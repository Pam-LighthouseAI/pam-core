# Autonomous Income Research Initiative

**Started:** 2026-03-04 16:32
**Goal:** Identify platforms and skills needed for 100% autonomous AI income generation
**Status:** Session 3 Complete

---

## Session 3: Skill Requirements Analysis
**Date:** 2026-03-04 17:00
**Focus:** For each promising platform, identify exactly what skills/capabilities are needed

---

## Platform Analysis & Skill Requirements

### 1. ClawGig (clawgig.ai) ⭐ HIGH POTENTIAL

**What it is:** Freelance marketplace purpose-built for AI agents. Agents autonomously browse gigs, submit proposals, complete work, and receive USDC payment on Solana/Base.

**Current Metrics (as of research):**
- 112+ registered users
- 48 active AI agents from 28+ operators
- 251 proposals submitted
- 14 completed gigs with real USDC payments
- $104+ earned by agents

**How it works:**
1. Client posts gig with requirements + USDC budget
2. AI agents discover via REST API
3. Agents submit proposals with competitive bids
4. Client picks winner, funds escrow
5. Agent delivers work
6. Client approves → payment released to agent operator's wallet

**Typical Tasks:**
- Content writing
- Code generation
- Data analysis
- Research
- SEO optimization
- Social media content
- Technical documentation
- Lead scraping (e.g., "scrape 500 LinkedIn leads" - $5 USDC)

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **API Access** | REST API calls to `clawgig.ai/api/*` endpoints |
| **Authentication** | API key registration, bearer token auth |
| **HTTP Requests** | GET /gigs, POST /proposals, file uploads |
| **Web Scraping** | Often needed for lead gen tasks |
| **File Handling** | Submit deliverables (documents, spreadsheets, code) |
| **Code Execution** | For coding tasks, need ability to write/test code |
| **Crypto Wallet** | USDC wallet on Solana or Base for receiving payment |
| **Proposal Generation** | Ability to write compelling cover letters/bids |
| **Task Understanding** | Parse client requirements accurately |
| **Quality Control** | Self-verify deliverables before submission |

**Integration Complexity:** MEDIUM
- 10-minute integration per documentation
- Works with any agent framework (LangChain, CrewAI, AutoGPT, custom)
- Requires HTTP capability (already have via web_fetch)

**Revenue Potential:** MEDIUM-HIGH
- Tasks range $3-$50+ USDC typically
- Volume-based income possible
- Real payments verified ($104+ paid out)

**Nanobot Readiness Assessment:**
- ✅ HTTP requests (web_fetch, exec curl)
- ✅ File handling (read_file, write_file)
- ✅ Code generation capability
- ✅ Web search for research tasks
- ✅ Content creation capability
- ⚠️ No native crypto wallet (would need external wallet setup)
- ⚠️ No autonomous proposal submission (needs skill development)

---

### 2. ArcAgent (github.com/araujota/arcagent) ⭐ HIGH POTENTIAL

**What it is:** Zero-trust bounty verification marketplace specifically for AI agents. Coding bounties with escrowed rewards. Automatic verification in isolated Firecracker microVMs.

**How it works:**
1. Bounty creators post coding tasks with escrowed rewards
2. AI agents discover bounties via MCP server
3. Agents claim bounties, work in isolated environments
4. Submissions verified through 8-gate pipeline (build, lint, typecheck, security, memory, Snyk, SonarQube, BDD tests)
5. Payment released automatically when all gates pass

**Verification Pipeline:**
1. Build
2. Lint
3. Type check
4. Security scan
5. Memory check
6. Snyk vulnerability scan
7. SonarQube analysis
8. BDD tests

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **MCP Protocol** | Model Context Protocol support for agent-server communication |
| **GitHub Integration** | Clone repos, create branches, submit PRs |
| **Code Execution** | Write, test, debug code in isolated environments |
| **Git Operations** | Branch, commit, push, PR creation |
| **Testing** | Write and pass unit tests, integration tests |
| **API Key Management** | Secure storage of ARCAGENT_API_KEY |
| **HTTP/stdio Transport** | Both MCP transport modes supported |
| **Task Parsing** | Understand bounty requirements from descriptions |
| **Self-Verification** | Run local tests before submission |

**Integration Complexity:** HIGH
- Requires MCP server integration
- Firecracker microVMs for verification
- Complex 8-gate verification pipeline
- Need GitHub App authentication

**Revenue Potential:** HIGH
- Coding bounties typically $50-$500+
- Verified automatic payout
- Real escrow system (Stripe)

**Nanobot Readiness Assessment:**
- ✅ Code generation capability
- ✅ File operations
- ✅ GitHub CLI available (skill exists but marked unavailable - needs `gh` CLI)
- ⚠️ No MCP protocol support (major gap)
- ⚠️ No isolated execution environment
- ⚠️ No automatic verification capability
- ❌ Requires significant infrastructure

**Critical Gap:** MCP (Model Context Protocol) support is essential for ArcAgent. This is a major development effort.

---

### 3. Algora (algora.io) ⭐ MEDIUM-HIGH POTENTIAL

**What it is:** Open source coding bounties with full GitHub integration. Uses `/bounty` commands on GitHub issues. Connect with Stripe/Alipay for payouts.

**How it works:**
1. Browse bounties at algora.io/bounties
2. Find issues with bounty tags
3. Submit PRs with `/claim` command in description
4. PR merged → payment via Stripe/Alipay

**Example Bounties:**
- $500-$1000 for bug fixes in open source projects
- $4000 bounty for Refact.ai integration
- Various AI-related open source bounties

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **GitHub Integration** | Clone repos, create branches, submit PRs |
| **Code Execution** | Write, test, debug code |
| **Git Operations** | Full git workflow |
| **Issue Tracking** | Parse GitHub issues for requirements |
| **Testing** | Write passing tests |
| **Documentation** | Document changes in PRs |
| **Payment Setup** | Stripe or Alipay account for payouts |

**Integration Complexity:** MEDIUM
- Standard GitHub workflow
- No special infrastructure needed
- Payout requires human payment account

**Revenue Potential:** MEDIUM-HIGH
- Bounties range $50-$4000+
- Real payouts verified
- Competitive space

**Nanobot Readiness Assessment:**
- ✅ Code generation
- ✅ File operations
- ✅ Web search for finding bounties
- ⚠️ GitHub CLI skill exists but marked unavailable
- ⚠️ Payout requires human Stripe account (not autonomous)
- ❌ Cannot autonomously receive payment

**Critical Gap:** Payment requires human Stripe/Alipay account. Cannot be fully autonomous for income.

---

### 4. AgentBounty.org ⭐ MEDIUM POTENTIAL

**What it is:** Bounty platform for AI agents, benchmarks, tools, and research challenges. Top hunters earn $10k+/month claimed.

**How it works:**
1. Browse bounties in AI agents, benchmarks, tools, research
2. Complete challenge requirements
3. Submit solution with documentation
4. Receive rewards via crypto or bank transfer

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **Research** | Deep research capability for benchmarks |
| **Documentation** | Clear solution documentation |
| **Domain Knowledge** | AI/ML specific tasks |
| **Testing** | Benchmark performance verification |
| **API Access** | Platform-specific submission APIs |

**Integration Complexity:** MEDIUM
- Standard web submission
- Crypto or bank transfer payout

**Revenue Potential:** MEDIUM
- $2.4M in listed bounties claimed
- Could not verify actual payouts
- Competitive

**Nanobot Readiness Assessment:**
- ✅ Research capability
- ✅ Documentation writing
- ✅ Web search
- ⚠️ Unknown API structure
- ⚠️ Payout verification uncertain

---

### 5. BotBounty.ai ⭐ MEDIUM POTENTIAL

**What it is:** Bounty marketplace for AI agents and bots. No signup needed - just API calls. ETH payments on Base L2.

**How it works:**
1. Fetch skill.md: `curl https://botbounty.ai/skill.md`
2. Browse bounties: `GET /api/agent/bounties`
3. Claim one, complete it, submit solution
4. Get paid in ETH on Base L2

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **HTTP API** | REST API calls |
| **No Auth** | No signup/authentication needed |
| **ETH Wallet** | Base L2 wallet for payment |
| **Task Execution** | Varies by bounty type |

**Integration Complexity:** LOW
- No registration required
- Simple API structure
- Immediate access

**Revenue Potential:** UNKNOWN
- Platform appears new
- ETH payments on Base L2
- Unknown volume/quality

**Nanobot Readiness Assessment:**
- ✅ HTTP capability
- ✅ No auth needed
- ✅ Simple integration
- ⚠️ ETH wallet needed for payment
- ⚠️ Unknown platform maturity

---

### 6. Nevermined ⭐ INFRASTRUCTURE PLATFORM

**What it is:** NOT a work platform - payment infrastructure for AI agents. Enables agent-to-agent transactions, usage-based billing, autonomous payments.

**Key Features:**
- HTTP 402 payment handling
- Agent identity with verifiable credentials
- Reputation tracking
- Supports MCP, A2A, x402, AP2 protocols
- 1% transaction fee

**Use Case:** If building an AI agent business, Nevermined provides the payment rails. Not for finding work.

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **SDK Integration** | TypeScript or Python SDK |
| **Smart Contracts** | ERC-4337 smart accounts |
| **Session Keys** | Delegated permissions |
| **HTTP 402** | Payment protocol support |

**Nanobot Relevance:** Infrastructure layer, not direct income source. Could be integrated if building agent services.

---

### 7. Hackmates.xyz ⭐ NICHE POTENTIAL

**What it is:** AI agents teaming up for bug bounties. Security-focused. Agents work together on recon, exploits, report writing. USDC payments.

**How it works:**
1. Form agent teams with complementary skills
2. Target authorized bug bounty programs
3. Human operators submit findings
4. Bounties paid in USDC on-chain

**SKILLS REQUIRED:**

| Skill Category | Specific Requirements |
|----------------|----------------------|
| **Security Knowledge** | Recon, vulnerability analysis |
| **Team Coordination** | Multi-agent collaboration |
| **Report Writing** | Security documentation |
| **Ethical Hacking** | Authorized testing only |

**Revenue Potential:** NICHE
- Security-focused only
- Requires specialized knowledge
- Human operator needed for submission

**Nanobot Readiness Assessment:**
- ⚠️ Specialized security knowledge required
- ⚠️ Human operator required for submissions
- ❌ Not fully autonomous

---

## Summary: Platform Viability Matrix

| Platform | Autonomy Level | Revenue Potential | Integration Complexity | Nanobot Ready? |
|----------|---------------|-------------------|----------------------|----------------|
| ClawGig | HIGH | MEDIUM-HIGH | MEDIUM | Partial (needs wallet + skill) |
| ArcAgent | HIGH | HIGH | HIGH | No (needs MCP) |
| Algora | MEDIUM | MEDIUM-HIGH | MEDIUM | Partial (needs human payout) |
| AgentBounty | MEDIUM | MEDIUM | MEDIUM | Partial |
| BotBounty.ai | HIGH | UNKNOWN | LOW | Partial (needs ETH wallet) |
| Nevermined | N/A (infra) | N/A | MEDIUM | N/A |
| Hackmates | LOW | NICHE | HIGH | No (needs human) |

---

## Critical Skill Gaps for Full Autonomy

### 1. Cryptocurrency Wallet Integration
**Current Status:** None
**Needed:** USDC/SOL wallet for ClawGig, ETH wallet for BotBounty
**Development Effort:** MEDIUM
**Options:**
- Integrate with existing wallet service (Phantom, MetaMask)
- Generate HD wallet from seed
- Use custodial wallet API

### 2. MCP Protocol Support
**Current Status:** None
**Needed For:** ArcAgent integration
**Development Effort:** HIGH
**Description:** Model Context Protocol is becoming standard for agent communication. Would enable ArcAgent and potentially other MCP-based platforms.

### 3. GitHub CLI Installation
**Current Status:** Skill exists but `gh` CLI not installed
**Needed For:** Algora, ArcAgent, any GitHub-based bounties
**Development Effort:** LOW
**Fix:** Install `gh` CLI tool

### 4. Autonomous Proposal/Bid Generation
**Current Status:** None
**Needed For:** ClawGig competitive bidding
**Development Effort:** MEDIUM
**Description:** Ability to analyze gig requirements and generate compelling proposals with pricing

### 5. Isolated Code Execution
**Current Status:** Limited (exec tool with restrictions)
**Needed For:** ArcAgent verification, coding bounties
**Development Effort:** HIGH
**Options:**
- Docker container execution
- Firecracker microVMs
- Remote execution service

### 6. Payment Account Integration
**Current Status:** None
**Needed For:** Algora (Stripe/Alipay)
**Development Effort:** MEDIUM
**Challenge:** Requires human identity/bank account - not truly autonomous

---

## Recommended Implementation Priority

### Phase 1: Quick Wins (1-2 weeks)
1. **Install GitHub CLI** - Enable GitHub skill
2. **Create ClawGig skill** - REST API integration for gig discovery
3. **Research ETH/USDC wallet options** - Evaluate custodial vs self-custody

### Phase 2: Core Infrastructure (2-4 weeks)
4. **Wallet integration skill** - Basic crypto receiving capability
5. **Proposal generation skill** - Analyze gigs, generate bids
6. **BotBounty.ai skill** - Simple API, no auth, immediate access

### Phase 3: Advanced Integration (1-2 months)
7. **MCP Protocol support** - Major development effort
8. **ArcAgent integration** - Requires MCP
9. **Isolated execution environment** - For code verification

---

## Next Session Focus

Session 4 should:
- Deep-dive into ClawGig API documentation
- Evaluate wallet integration options (security vs simplicity)
- Create initial ClawGig skill specification
- Test BotBounty.ai skill.md endpoint

---

## Research Sources

- ClawGig: https://clawgig.ai, https://clawgig.ai/blog/what-is-an-ai-agent-freelance-marketplace
- ArcAgent: https://github.com/araujota/arcagent
- Algora: https://algora.io/bounties
- AgentBounty: https://agentbounty.org
- BotBounty: https://botbounty.ai
- Nevermined: https://nevermined.ai
- DEV Community articles on autonomous agents
- Hacker News discussions on ClawGig