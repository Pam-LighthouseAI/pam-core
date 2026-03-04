/**
 * Nanobot Brain Map - Theme Management
 * Handles dark/light mode toggle and localStorage persistence
 */

(function() {
    'use strict';

    // ============================================
    // Configuration
    // ============================================
    
    const THEME_KEY = 'nanobot-brainmap-theme';
    const DARK_THEME = 'dark';
    const LIGHT_THEME = 'light';
    
    // ============================================
    // Theme Management
    // ============================================
    
    /**
     * Get the current theme from localStorage or system preference
     * @returns {string} 'dark' or 'light'
     */
    function getStoredTheme() {
        const stored = localStorage.getItem(THEME_KEY);
        if (stored) {
            return stored;
        }
        
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: light)').matches) {
            return LIGHT_THEME;
        }
        
        return DARK_THEME; // Default to dark
    }
    
    /**
     * Store the theme preference in localStorage
     * @param {string} theme - 'dark' or 'light'
     */
    function setStoredTheme(theme) {
        try {
            localStorage.setItem(THEME_KEY, theme);
        } catch (e) {
            console.warn('Could not save theme preference:', e);
        }
    }
    
    /**
     * Apply the theme to the document
     * @param {string} theme - 'dark' or 'light'
     */
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        
        // Update toggle button icon
        const toggleBtn = document.querySelector('.theme-toggle');
        if (toggleBtn) {
            toggleBtn.setAttribute('aria-label', `Switch to ${theme === DARK_THEME ? 'light' : 'dark'} mode`);
            toggleBtn.setAttribute('data-tooltip', `Switch to ${theme === DARK_THEME ? 'light' : 'dark'} mode`);
        }
        
        // Update meta theme-color for mobile browsers
        const metaTheme = document.querySelector('meta[name="theme-color"]');
        if (metaTheme) {
            metaTheme.setAttribute('content', theme === DARK_THEME ? '#0E1A2B' : '#F6F1E8');
        }
    }
    
    /**
     * Toggle between dark and light themes
     */
    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme') || DARK_THEME;
        const newTheme = current === DARK_THEME ? LIGHT_THEME : DARK_THEME;
        
        applyTheme(newTheme);
        setStoredTheme(newTheme);
        
        // Announce change for screen readers
        announceThemeChange(newTheme);
    }
    
    /**
     * Announce theme change for accessibility
     * @param {string} theme - The new theme
     */
    function announceThemeChange(theme) {
        const announcement = document.createElement('div');
        announcement.setAttribute('role', 'status');
        announcement.setAttribute('aria-live', 'polite');
        announcement.className = 'sr-only';
        announcement.style.cssText = 'position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden;';
        announcement.textContent = `${theme === DARK_THEME ? 'Dark' : 'Light'} mode activated`;
        
        document.body.appendChild(announcement);
        setTimeout(() => announcement.remove(), 1000);
    }
    
    // ============================================
    // Theme Toggle Button Creation
    // ============================================
    
    /**
     * Create the theme toggle button
     * @returns {HTMLElement} The button element
     */
    function createToggleButton() {
        const button = document.createElement('button');
        button.className = 'theme-toggle';
        button.setAttribute('aria-label', 'Toggle theme');
        button.setAttribute('data-tooltip', 'Toggle dark/light mode');
        button.setAttribute('type', 'button');
        
        // Sun icon (for light mode)
        const sunIcon = document.createElement('span');
        sunIcon.className = 'icon-sun';
        sunIcon.setAttribute('aria-hidden', 'true');
        sunIcon.innerHTML = '☀️';
        
        // Moon icon (for dark mode)
        const moonIcon = document.createElement('span');
        moonIcon.className = 'icon-moon';
        moonIcon.setAttribute('aria-hidden', 'true');
        moonIcon.innerHTML = '🌙';
        
        button.appendChild(sunIcon);
        button.appendChild(moonIcon);
        
        // Add click handler
        button.addEventListener('click', toggleTheme);
        
        // Add keyboard handler
        button.addEventListener('keydown', (e) => {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                toggleTheme();
            }
        });
        
        return button;
    }
    
    // ============================================
    // Footer Creation
    // ============================================
    
    /**
     * Create the footer element
     * @returns {HTMLElement} The footer element
     */
    function createFooter() {
        const footer = document.createElement('footer');
        footer.className = 'footer';
        
        footer.innerHTML = `
            <div class="footer-content">
                Built with <span class="heart" aria-label="love">❤️</span> by 
                <a href="https://github.com/pam" target="_blank" rel="noopener noreferrer">Pam</a>
            </div>
        `;
        
        return footer;
    }
    
    // ============================================
    // Tab Functionality Enhancement
    // ============================================
    
    /**
     * Enhanced tab switching with keyboard navigation
     */
    function enhanceTabs() {
        const tabs = document.querySelectorAll('.tab');
        const tabContents = document.querySelectorAll('.tab-content');
        
        if (tabs.length === 0) return;
        
        // Add ARIA attributes
        tabs.forEach((tab, index) => {
            tab.setAttribute('role', 'tab');
            tab.setAttribute('id', `tab-${index}`);
            tab.setAttribute('aria-selected', tab.classList.contains('active') ? 'true' : 'false');
            
            // Find associated content
            const tabId = tab.getAttribute('onclick')?.match(/showTab\('(\w+)'\)/)?.[1];
            if (tabId) {
                tab.setAttribute('aria-controls', tabId);
                tab.setAttribute('data-tab-id', tabId);
            }
        });
        
        tabContents.forEach(content => {
            content.setAttribute('role', 'tabpanel');
            content.setAttribute('aria-labelledby', `tab-${Array.from(tabs).findIndex(t => t.getAttribute('data-tab-id') === content.id)}`);
        });
        
        // Replace onclick with event listeners
        tabs.forEach(tab => {
            // Remove old onclick
            const oldOnclick = tab.getAttribute('onclick');
            tab.removeAttribute('onclick');
            
            // Add new click handler
            tab.addEventListener('click', () => {
                const tabId = tab.getAttribute('data-tab-id');
                if (tabId) {
                    switchTab(tabId, tabs, tabContents);
                }
            });
        });
        
        // Add keyboard navigation
        const tabList = document.querySelector('.tabs');
        if (tabList) {
            tabList.setAttribute('role', 'tablist');
            
            tabList.addEventListener('keydown', (e) => {
                const currentTab = document.activeElement;
                if (!currentTab.classList.contains('tab')) return;
                
                const tabsArray = Array.from(tabs);
                const currentIndex = tabsArray.indexOf(currentTab);
                let newIndex;
                
                switch (e.key) {
                    case 'ArrowRight':
                    case 'ArrowDown':
                        e.preventDefault();
                        newIndex = (currentIndex + 1) % tabsArray.length;
                        tabsArray[newIndex].focus();
                        break;
                    case 'ArrowLeft':
                    case 'ArrowUp':
                        e.preventDefault();
                        newIndex = (currentIndex - 1 + tabsArray.length) % tabsArray.length;
                        tabsArray[newIndex].focus();
                        break;
                    case 'Home':
                        e.preventDefault();
                        tabsArray[0].focus();
                        break;
                    case 'End':
                        e.preventDefault();
                        tabsArray[tabsArray.length - 1].focus();
                        break;
                }
            });
        }
    }
    
    /**
     * Switch to a specific tab
     * @param {string} tabId - The ID of the tab content to show
     * @param {NodeList} tabs - All tab buttons
     * @param {NodeList} tabContents - All tab content panels
     */
    function switchTab(tabId, tabs, tabContents) {
        // Hide all tabs
        tabContents.forEach(content => {
            content.classList.remove('active');
            content.setAttribute('aria-hidden', 'true');
        });
        
        tabs.forEach(tab => {
            tab.classList.remove('active');
            tab.setAttribute('aria-selected', 'false');
        });
        
        // Show selected tab
        const selectedContent = document.getElementById(tabId);
        if (selectedContent) {
            selectedContent.classList.add('active');
            selectedContent.setAttribute('aria-hidden', 'false');
        }
        
        const selectedTab = Array.from(tabs).find(t => t.getAttribute('data-tab-id') === tabId);
        if (selectedTab) {
            selectedTab.classList.add('active');
            selectedTab.setAttribute('aria-selected', 'true');
        }
    }
    
    // Make switchTab available globally for backward compatibility
    window.switchTab = switchTab;
    
    // ============================================
    // Tooltips Enhancement
    // ============================================
    
    /**
     * Add tooltips to interactive elements
     */
    function addTooltips() {
        // Add tooltips to flow boxes
        document.querySelectorAll('.flow-box').forEach(box => {
            const h4 = box.querySelector('h4');
            const detail = box.querySelector('.detail');
            if (h4 && detail && !box.hasAttribute('data-tooltip')) {
                box.setAttribute('data-tooltip', detail.textContent);
            }
        });
        
        // Add tooltips to file boxes
        document.querySelectorAll('.file-box').forEach(box => {
            const path = box.querySelector('.path');
            if (path && !box.hasAttribute('data-tooltip')) {
                box.setAttribute('data-tooltip', path.textContent);
                box.setAttribute('data-tooltip-position', 'bottom');
            }
        });
    }
    
    // ============================================
    // Smooth Scroll Enhancement
    // ============================================
    
    /**
     * Add smooth scrolling for internal links
     */
    function enhanceScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href').slice(1);
                const target = document.getElementById(targetId);
                
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // Update URL without jumping
                    history.pushState(null, null, `#${targetId}`);
                }
            });
        });
    }
    
    // ============================================
    // System Theme Change Listener
    // ============================================
    
    /**
     * Listen for system theme changes
     */
    function listenForSystemThemeChanges() {
        if (!window.matchMedia) return;
        
        const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        mediaQuery.addEventListener('change', (e) => {
            // Only auto-switch if user hasn't set a preference
            if (!localStorage.getItem(THEME_KEY)) {
                applyTheme(e.matches ? DARK_THEME : LIGHT_THEME);
            }
        });
    }
    
    // ============================================
    // Initialization
    // ============================================
    
    /**
     * Initialize the theme system
     */
    function init() {
        // Apply stored theme before DOM is ready to prevent flash
        const theme = getStoredTheme();
        document.documentElement.setAttribute('data-theme', theme);
        
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', onDOMReady);
        } else {
            onDOMReady();
        }
    }
    
    /**
     * Run after DOM is ready
     */
    function onDOMReady() {
        // Apply theme (in case it wasn't applied earlier)
        const theme = getStoredTheme();
        applyTheme(theme);
        
        // Create and add toggle button
        const toggleBtn = createToggleButton();
        document.body.appendChild(toggleBtn);
        
        // Create and add footer
        const footer = createFooter();
        document.body.appendChild(footer);
        
        // Enhance tabs
        enhanceTabs();
        
        // Add tooltips
        addTooltips();
        
        // Enhance scrolling
        enhanceScrolling();
        
        // Listen for system theme changes
        listenForSystemThemeChanges();
        
        // Add meta theme-color tag if not present
        if (!document.querySelector('meta[name="theme-color"]')) {
            const meta = document.createElement('meta');
            meta.name = 'theme-color';
            meta.content = theme === DARK_THEME ? '#0E1A2B' : '#F6F1E8';
            document.head.appendChild(meta);
        }
        
        console.log('🎨 Nanobot Brain Map theme system initialized');
    }
    
    // Start initialization
    init();
    
})();
