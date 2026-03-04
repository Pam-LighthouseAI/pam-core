# Multi-Agent Web Scraping Framework

## Overview
A structured approach for coordinating multiple AI agents (like Pam & Dwight) to efficiently execute web scraping projects.

## Agent Roles

### **Pam (Content/Coordination Agent)**
- **Responsibilities**:
  - Project planning & task decomposition
  - Data validation & quality assurance
  - Communication with client/user
  - Final report generation
- **Tools**:
  - Web search & research
  - File I/O (CSV, JSON, Markdown)
  - Data validation scripts
  - Communication protocols

### **Dwight (Technical/Execution Agent)**
- **Responsibilities**:
  - Technical implementation
  - Scraping script development
  - Error handling & retry logic
  - Performance optimization
- **Tools**:
  - Python (BeautifulSoup, Scrapy, Selenium)
  - Proxy management
  - Rate limiting implementation
  - Data storage systems

## Workflow

### Phase 1: Discovery & Planning
1. **Requirements Gathering** (Pam)
   - Define scraping targets
   - Identify data points needed
   - Set success criteria
2. **Technical Assessment** (Dwight)
   - Analyze site structure
   - Identify anti-scraping measures
   - Estimate resource requirements

### Phase 2: Implementation
1. **Environment Setup** (Dwight)
   - Configure scraping tools
   - Set up proxy rotation
   - Implement error handling
2. **Template Creation** (Pam)
   - Design data schema
   - Create validation rules
   - Set up reporting templates

### Phase 3: Execution
1. **Parallel Processing** (Both)
   - Dwight: Runs scraping jobs
   - Pam: Monitors progress & validates samples
2. **Quality Control** (Pam)
   - Spot-check data quality
   - Flag issues for Dwight
   - Update validation rules

### Phase 4: Delivery
1. **Data Packaging** (Dwight)
   - Clean & format data
   - Export to requested formats
   - Create metadata files
2. **Reporting** (Pam)
   - Generate summary report
   - Document methodology
   - Provide insights & recommendations

## Communication Protocol

### Daily Sync Format
```json
{
  "agent": "Pam/Dwight",
  "timestamp": "ISO-8601",
  "status": "in_progress/completed/blocked",
  "progress": "X/Y items processed",
  "issues": ["list of problems"],
  "next_steps": ["immediate actions"]
}
```

### File Sharing Structure
```
project/
├── config/           # Configuration files
├── scripts/          # Scraping scripts
├── data/             # Raw & processed data
├── logs/             # Execution logs
└── reports/          # Progress & final reports
```

## Error Handling

### Common Issues & Resolution
1. **IP Blocking**
   - Dwight: Rotate proxies, implement delays
   - Pam: Monitor success rates, adjust targets

2. **Site Structure Changes**
   - Dwight: Update selectors, add fallbacks
   - Pam: Validate data consistency, flag anomalies

3. **Data Quality Issues**
   - Pam: Identify patterns in bad data
   - Dwight: Fix parsing logic, add validation

## Performance Optimization

### Scaling Strategies
- **Vertical Scaling**: Increase agent capabilities
- **Horizontal Scaling**: Add more specialized agents
- **Parallel Processing**: Split domains/URLs among agents

### Monitoring Metrics
- Success rate (%)
- Items processed per hour
- Data quality score
- Resource utilization

## Tools & Technologies

### Recommended Stack
- **Scraping**: Scrapy, Playwright, Puppeteer
- **Data Storage**: CSV, JSON, SQLite, Parquet
- **Communication**: Webhooks, shared file systems, message queues
- **Monitoring**: Custom dashboards, logging systems

## Best Practices

1. **Ethical Scraping**
   - Respect robots.txt
   - Implement reasonable delays
   - Cache data when possible

2. **Data Management**
   - Version control for scripts
   - Backup raw data
   - Document all transformations

3. **Agent Coordination**
   - Clear role definitions
   - Regular checkpoints
   - Shared documentation

## Template Files

### Project Checklist (`checklist.md`)
```markdown
# Project: [Name]

## Setup
- [ ] Environment configured
- [ ] Target sites analyzed
- [ ] Data schema defined

## Execution
- [ ] Scraping scripts ready
- [ ] Validation rules set
- [ ] Monitoring in place

## Delivery
- [ ] Data cleaned & formatted
- [ ] Reports generated
- [ ] Client approval received
```

### Status Report Template (`status_template.md`)
```markdown
# Status Report: [Date]

## Progress
- Items processed: X/Y
- Success rate: XX%
- Issues resolved: #

## Current Focus
- [Brief description]

## Next Steps
1. [Action 1]
2. [Action 2]
3. [Action 3]

## Blockers
- [List any blockers]
```

---

**Framework Version**: 1.0
**Last Updated**: 2026-02-24
**Agents**: Pam (Content/Coordination), Dwight (Technical/Execution)
```