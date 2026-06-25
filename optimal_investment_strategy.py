# Stock data: price (investment), expected return, risk
stocks = {
 "StockA": {"price": 50, "return": 10, "risk": 5},
 "StockB": {"price": 40, "return": 8, "risk": 4},
 "StockC": {"price": 30, "return": 6, "risk": 3},
 "StockD": {"price": 20, "return": 4, "risk": 2}
}
budget = 100
max_risk = 10
stock_list = list(stocks.keys())
n = len(stock_list)
# -----------------------------
# Step 1: Display Stock Details
# -----------------------------
output = []
output.append("STOCK DETAILS:")
output.append("Name\tPrice\tReturn\tRisk")
for s in stocks:
 output.append(f"{s}\t{stocks[s]['price']}\t{stocks[s]['return']}\t{stocks[s]['risk']}")
# -----------------------------
# Step 2: Budget
# -----------------------------
output.append(f"\nAVAILABLE BUDGET: {budget}")
output.append(f"MAXIMUM ALLOWED RISK: {max_risk}")
# -----------------------------
# Step 3: Generate ALL combinations
# -----------------------------
from itertools import combinations
output.append("\nPOSSIBLE ALLOCATION COMBINATIONS:")
best_return = 0
best_combination = []
best_risk = 0
for r in range(1, n+1):
 for combo in combinations(stock_list, r):
 total_price = sum(stocks[s]["price"] for s in combo)
 total_return = sum(stocks[s]["return"] for s in combo)
 total_risk = sum(stocks[s]["risk"] for s in combo)
 output.append(f"{combo} -> Cost={total_price}, Return={total_return}, 
Risk={total_risk}")
 # Check constraints
 if total_price <= budget and total_risk <= max_risk:
 if total_return > best_return:
 best_return = total_return
 best_combination = combo
 best_risk = total_risk
# -----------------------------
# Step 4: Final Optimal Allocation
# -----------------------------
output.append("\nFINAL OPTIMAL ALLOCATION:")
for s in best_combination:
 output.append(s)
# -----------------------------
# Step 5: Final Result
# -----------------------------
output.append(f"\nMAXIMUM EXPECTED RETURN: {best_return}")
output.append(f"CORRESPONDING RISK: {best_risk}")
# -----------------------------
# Step 6: Constraint Checking
# -----------------------------
total_price = sum(stocks[s]["price"] for s in best_combination)
output.append("\nCONSTRAINT CHECKING:")
if total_price <= budget:
 output.append("✔ Budget constraint satisfied")
else:
 output.append("✘ Budget constraint violated")
if best_risk <= max_risk:
 output.append("✔ Risk constraint satisfied")
else:
 output.append("✘ Risk constraint violated")
output.append("✔ Investment proportions valid (0/1 selection)")
# -----------------------------
# Step 7: Time Complexity
# -----------------------------
output.append("\nTIME COMPLEXITY:")
output.append("O(2^n) (Generating all subsets)")
# Step 8: Save Output
# -----------------------------
with open("portfolio_optimization_output.txt", "w", encoding="utf-8") as f:
 f.write("\n".join(output))
# Print output
print("\n".join(output))