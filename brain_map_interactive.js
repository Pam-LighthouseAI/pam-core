/**
 * Nanobot Brain Map - Interactive Features
 * Built by Pam
 */

(function() {
    'use strict';
    
    // ============================================
    // SIMULATE MESSAGE FLOW
    // ============================================
    
    class MessageFlowSimulator {
        constructor() {
            this.flowBoxes = document.querySelectorAll('.flow-box');
            this.arrows = document.querySelectorAll('.arrow');
            this.isPlaying = false;
            this.currentStep = 0;
            this.createSimulateButton();
            this.createResetButton();
        }
        
        createSimulateButton() {
            const button = document.createElement('button');
            button.id = 'simulate-btn';
            button.className = 'simulate-button';
            button.innerHTML = '▶️ Simulate Message Flow';
            button.setAttribute('data-tooltip', 'Watch a message travel through the system');
            
            const flowSection = document.querySelector('#flow .section');
            if (flowSection) {
                flowSection.insertBefore(button, flowSection.querySelector('.flow-container'));
            }
            
            button.addEventListener('click', () => this.simulate());
        }
        
        createResetButton() {
            const button = document.createElement('button');
            button.id = 'reset-btn';
            button.className = 'reset-button';
            button.innerHTML = '🔄 Reset';
            button.setAttribute('data-tooltip', 'Reset the animation');
            button.style.display = 'none';
            
            const simulateBtn = document.getElementById('simulate-btn');
            if (simulateBtn && simulateBtn.parentNode) {
                simulateBtn.parentNode.insertBefore(button, simulateBtn.nextSibling);
            }
            
            button.addEventListener('click', () => this.reset());
        }
        
        async simulate() {
            if (this.isPlaying) return;
            this.isPlaying = true;
            
            const simulateBtn = document.getElementById('simulate-btn');
            const resetBtn = document.getElementById('reset-btn');
            
            if (simulateBtn) {
                simulateBtn.disabled = true;
                simulateBtn.innerHTML = '⏳ Simulating...';
            }
            if (resetBtn) resetBtn.style.display = 'inline-block';
            
            // Reset first
            this.reset(false);
            
            // Animate each flow row in sequence
            const flowRows = document.querySelectorAll('.flow-row');
            
            for (let i = 0; i < flowRows.length; i++) {
                const row = flowRows[i];
                const boxes = row.querySelectorAll('.flow-box');
                const arrows = row.querySelectorAll('.arrow');
                
                // Animate boxes in this row
                for (let j = 0; j < boxes.length; j++) {
                    await this.delay(300);
                    boxes[j].classList.add('active');
                    this.pulse(boxes[j]);
                    
                    // Animate arrow after box (if exists)
                    if (arrows[j]) {
                        await this.delay(150);
                        arrows[j].classList.add('active');
                    }
                }
                
                // Small pause between rows
                await this.delay(500);
            }
            
            // Show completion
            await this.delay(300);
            if (simulateBtn) {
                simulateBtn.innerHTML = '✅ Complete!';
            }
            
            this.isPlaying = false;
        }
        
        reset(showButton = true) {
            this.flowBoxes.forEach(box => {
                box.classList.remove('active');
            });
            this.arrows.forEach(arrow => {
                arrow.classList.remove('active');
            });
            
            const simulateBtn = document.getElementById('simulate-btn');
            if (simulateBtn && showButton) {
                simulateBtn.disabled = false;
                simulateBtn.innerHTML = '▶️ Simulate Message Flow';
            }
            
            if (!showButton) {
                const resetBtn = document.getElementById('reset-btn');
                if (resetBtn) resetBtn.style.display = 'none';
            }
        }
        
        pulse(element) {
            element.classList.add('pulse');
            setTimeout(() => element.classList.remove('pulse'), 600);
        }
        
        delay(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
        }
    }
    
    // ============================================
    // CLICK TO EXPAND DETAILS
    // ============================================
    
    class DetailExpander {
        constructor() {
            this.createModal();
            this.attachClickHandlers();
        }
        
        createModal() {
            const modal = document.createElement('div');
            modal.id = 'detail-modal';
            modal.className = 'modal';
            modal.innerHTML = `
                <div class="modal-content">
                    <button class="modal-close" data-tooltip="Close">&times;</button>
                    <div class="modal-header">
                        <h3 id="modal-title"></h3>
                        <code id="modal-path"></code>
                    </div>
                    <div id="modal-body"></div>
                </div>
            `;
            document.body.appendChild(modal);
            
            // Close handlers
            modal.querySelector('.modal-close').addEventListener('click', () => this.closeModal());
            modal.addEventListener('click', (e) => {
                if (e.target === modal) this.closeModal();
            });
            
            // Escape key
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') this.closeModal();
            });
        }
        
        attachClickHandlers() {
            // File boxes
            document.querySelectorAll('.file-box').forEach(box => {
                box.classList.add('clickable');
                box.addEventListener('click', () => this.showFileDetail(box));
            });
            
            // Code tree files
            document.querySelectorAll('.code-tree .file').forEach(file => {
                file.classList.add('clickable');
                file.addEventListener('click', () => this.showCodeDetail(file));
            });
        }
        
        showFileDetail(box) {
            const title = box.querySelector('h3')?.textContent || 'Details';
            const path = box.querySelector('.path')?.textContent || '';
            const description = box.querySelector('p')?.textContent || '';
            const list = box.querySelector('ul')?.innerHTML || '';
            
            document.getElementById('modal-title').textContent = title;
            document.getElementById('modal-path').textContent = path;
            document.getElementById('modal-body').innerHTML = `
                <p>${description}</p>
                ${list ? `<ul>${list}</ul>` : ''}
            `;
            
            this.openModal();
        }
        
        showCodeDetail(file) {
            const text = file.textContent.trim();
            const parts = text.split('#');
            const filename = parts[0].trim();
            const desc = parts[1] ? parts[1].trim() : '';
            
            document.getElementById('modal-title').textContent = filename;
            document.getElementById('modal-path').textContent = 'nanobot/' + filename;
            document.getElementById('modal-body').innerHTML = `
                <p>${desc || 'Part of the nanobot codebase.'}</p>
            `;
            
            this.openModal();
        }
        
        openModal() {
            document.getElementById('detail-modal').classList.add('open');
            document.body.style.overflow = 'hidden';
        }
        
        closeModal() {
            document.getElementById('detail-modal').classList.remove('open');
            document.body.style.overflow = '';
        }
    }
    
    // ============================================
    // HOVER HIGHLIGHTS
    // ============================================
    
    class HoverHighlighter {
        constructor() {
            this.attachHoverHandlers();
        }
        
        attachHoverHandlers() {
            // Flow boxes highlight related elements
            document.querySelectorAll('.flow-box').forEach(box => {
                box.addEventListener('mouseenter', () => this.highlightRelated(box));
                box.addEventListener('mouseleave', () => this.clearHighlights());
            });
            
            // File boxes
            document.querySelectorAll('.file-box').forEach(box => {
                box.addEventListener('mouseenter', () => box.classList.add('hover'));
                box.addEventListener('mouseleave', () => box.classList.remove('hover'));
            });
        }
        
        highlightRelated(box) {
            const type = this.getBoxType(box);
            
            // Highlight all boxes of same type
            document.querySelectorAll(`.flow-box.${type}`).forEach(b => {
                b.classList.add('highlighted');
            });
            
            // Add glow to current
            box.classList.add('glow');
        }
        
        clearHighlights() {
            document.querySelectorAll('.flow-box').forEach(box => {
                box.classList.remove('highlighted', 'glow');
            });
        }
        
        getBoxType(box) {
            const classes = ['user', 'channel', 'bus', 'agent', 'context', 'llm', 'tools', 'soul', 'memory', 'skills'];
            for (const cls of classes) {
                if (box.classList.contains(cls)) return cls;
            }
            return '';
        }
    }
    
    // ============================================
    // SEARCH FUNCTIONALITY
    // ============================================
    
    class SearchBar {
        constructor() {
            this.createSearchBar();
            this.index = this.buildIndex();
        }
        
        createSearchBar() {
            const container = document.createElement('div');
            container.className = 'search-container';
            container.innerHTML = `
                <input type="text" id="search-input" placeholder="🔍 Search files, components..." data-tooltip="Search the brain map">
                <div id="search-results" class="search-results"></div>
            `;
            
            const header = document.querySelector('.container h1');
            if (header && header.parentNode) {
                header.parentNode.insertBefore(container, header.nextSibling.nextSibling);
            }
            
            const input = document.getElementById('search-input');
            input?.addEventListener('input', (e) => this.search(e.target.value));
            input?.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    input.value = '';
                    this.clearResults();
                }
            });
        }
        
        buildIndex() {
            const index = [];
            
            // Index file boxes
            document.querySelectorAll('.file-box').forEach(box => {
                index.push({
                    element: box,
                    title: box.querySelector('h3')?.textContent || '',
                    path: box.querySelector('.path')?.textContent || '',
                    content: box.textContent.toLowerCase(),
                    tab: this.findParentTab(box)
                });
            });
            
            // Index code tree files
            document.querySelectorAll('.code-tree .file').forEach(file => {
                index.push({
                    element: file,
                    title: file.textContent.split('#')[0].trim(),
                    path: '',
                    content: file.textContent.toLowerCase(),
                    tab: 'code'
                });
            });
            
            // Index flow boxes
            document.querySelectorAll('.flow-box').forEach(box => {
                index.push({
                    element: box,
                    title: box.querySelector('h4')?.textContent || '',
                    path: box.querySelector('.detail')?.textContent || '',
                    content: box.textContent.toLowerCase(),
                    tab: 'flow'
                });
            });
            
            return index;
        }
        
        findParentTab(element) {
            const tab = element.closest('.tab-content');
            return tab?.id || '';
        }
        
        search(query) {
            const results = document.getElementById('search-results');
            if (!results) return;
            
            if (!query.trim()) {
                this.clearResults();
                return;
            }
            
            const q = query.toLowerCase();
            const matches = this.index.filter(item => 
                item.title.toLowerCase().includes(q) ||
                item.path.toLowerCase().includes(q) ||
                item.content.includes(q)
            ).slice(0, 8);
            
            if (matches.length === 0) {
                results.innerHTML = '<div class="search-no-results">No results found</div>';
                return;
            }
            
            results.innerHTML = matches.map((item, i) => `
                <div class="search-result" data-index="${i}">
                    <strong>${item.title}</strong>
                    ${item.path ? `<br><code>${item.path}</code>` : ''}
                    <span class="search-tab">${item.tab}</span>
                </div>
            `).join('');
            
            // Click handlers
            results.querySelectorAll('.search-result').forEach((el, i) => {
                el.addEventListener('click', () => {
                    this.selectResult(matches[i]);
                });
            });
        }
        
        selectResult(item) {
            // Switch to correct tab
            if (item.tab) {
                const tabBtn = document.querySelector(`[data-tab-id="${item.tab}"]`);
                if (tabBtn) tabBtn.click();
            }
            
            // Scroll to element
            setTimeout(() => {
                item.element.scrollIntoView({ behavior: 'smooth', block: 'center' });
                item.element.classList.add('search-highlight');
                setTimeout(() => item.element.classList.remove('search-highlight'), 2000);
            }, 100);
            
            this.clearResults();
            const input = document.getElementById('search-input');
            if (input) input.value = '';
        }
        
        clearResults() {
            const results = document.getElementById('search-results');
            if (results) results.innerHTML = '';
        }
    }
    
    // ============================================
    // COLLAPSIBLE SECTIONS
    // ============================================
    
    class CollapsibleSections {
        constructor() {
            this.makeCollapsible();
        }
        
        makeCollapsible() {
            document.querySelectorAll('.section-title').forEach(title => {
                title.classList.add('collapsible-title');
                
                // Add toggle indicator
                const indicator = document.createElement('span');
                indicator.className = 'collapse-indicator';
                indicator.innerHTML = '▼';
                title.insertBefore(indicator, title.firstChild);
                
                title.addEventListener('click', () => this.toggle(title));
            });
        }
        
        toggle(title) {
            const section = title.parentElement;
            const isCollapsed = section.classList.toggle('collapsed');
            
            const indicator = title.querySelector('.collapse-indicator');
            if (indicator) {
                indicator.innerHTML = isCollapsed ? '▶' : '▼';
            }
        }
    }
    
    // ============================================
    // INITIALIZE
    // ============================================
    
    function init() {
        // Wait for DOM
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initFeatures);
        } else {
            initFeatures();
        }
    }
    
    function initFeatures() {
        // Small delay to ensure theme JS has run
        setTimeout(() => {
            new MessageFlowSimulator();
            new DetailExpander();
            new HoverHighlighter();
            new SearchBar();
            new CollapsibleSections();
            console.log('🧠 Nanobot Brain Map interactive features loaded');
        }, 100);
    }
    
    init();
    
})();
