from goal_tracker import GoalTracker, MetricDirection, Goal

tracker = GoalTracker()

# Create main goal
goal = tracker.create_goal(
    "AI Automation Studio: $100/Month Revenue",
    description="Achieve consistent $100/month income within 6 months",
    deadline_days=180,  # 6 months
    priority=10
)

# Add metrics
goal.add_metric("monthly_revenue", MetricDirection.TARGET, target=100, unit="USD")
goal.add_metric("paying_clients", MetricDirection.MAXIMIZE, target=3)
goal.add_metric("portfolio_projects", MetricDirection.MAXIMIZE, target=5)
goal.add_metric("outreach_messages", MetricDirection.MAXIMIZE, target=50)
goal.add_metric("proposals_sent", MetricDirection.MAXIMIZE, target=10)

# Add milestones (using value-based milestones)
goal.add_milestone("Month 1: Foundation complete", value=0)
goal.add_milestone("Month 2: Portfolio live, outreach started", value=0)
goal.add_milestone("Month 3: First paying client", value=1)
goal.add_milestone("Month 4: $50/month revenue", value=50)
goal.add_milestone("Month 5: $75/month revenue", value=75)
goal.add_milestone("Month 6: $100/month revenue achieved", value=100)

# Add strategies
goal.add_strategy("Build portfolio website", "Create a professional site showcasing AI automation services")
goal.add_strategy("Define service offerings", "Package services into clear, sellable products")
goal.add_strategy("Outreach to small businesses", "Contact local businesses who could benefit from AI automation")
goal.add_strategy("Leverage existing network", "Ask friends and contacts for referrals")
goal.add_strategy("Create case studies", "Document successful projects to build credibility")

# Initialize starting values
goal.record("monthly_revenue", 0, "Starting point")
goal.record("paying_clients", 0, "Starting point")
goal.record("portfolio_projects", 0, "Starting point")
goal.record("outreach_messages", 0, "Starting point")
goal.record("proposals_sent", 0, "Starting point")

# Save
tracker.save()

print("\n" + "="*55)
print("  🎯 AI AUTOMATION STUDIO - REVENUE GOAL SET")
print("="*55)
print(f"\n  Target: $100/month by September 2, 2026")
print(f"  Priority: 10/10")
print(f"\n  📊 Metrics to Track:")
print(f"     • Monthly Revenue: $0 → $100")
print(f"     • Paying Clients: 0 → 3")
print(f"     • Portfolio Projects: 0 → 5")
print(f"     • Outreach Messages: 0 → 50")
print(f"     • Proposals Sent: 0 → 10")
print(f"\n  🎯 Milestones:")
print(f"     ○ Month 1: Foundation complete")
print(f"     ○ Month 2: Portfolio live, outreach started")
print(f"     ○ Month 3: First paying client")
print(f"     ○ Month 4: $50/month revenue")
print(f"     ○ Month 5: $75/month revenue")
print(f"     ○ Month 6: $100/month revenue achieved")
print(f"\n  💡 Strategies Available:")
for s in goal.strategies:
    print(f"     • {s.name}: {s.description}")
print("="*55)
