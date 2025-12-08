import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\program_py\insurance.csv")

# Fix column naming issue automatically (if 'expenses' is present)
if "expenses" in df.columns and "charges" not in df.columns:
    df.rename(columns={"expenses": "charges"}, inplace=True)

print("Columns detected:", df.columns)

# ─────────────────────────────────────────────
# SQL Equivalent (for documentation)
print("\n📌 SQL Query: Average charges by region and smoking status")
print("""
SELECT 
    region,
    smoker,
    AVG(charges) AS avg_charges
FROM insurance
GROUP BY region, smoker
ORDER BY region, smoker;
""")
# ─────────────────────────────────────────────

# 1. Boxplot (Charges by Smoker vs Non-Smoker)
plt.figure()
sns.boxplot(x="smoker", y="charges", data=df, palette="Set2")
plt.title("Charges by Smoker vs Non-Smoker")
plt.tight_layout()
plt.show()
plt.close()

# 2. Regression Plot (Age vs Charges)
plt.figure()
sns.regplot(x="age", y="charges", data=df, scatter_kws={'alpha':0.5})
plt.title("Regression: Age vs Charges")
plt.tight_layout()
plt.show()
plt.close()

# 3. Heatmap (Correlation)
plt.figure(figsize=(6,4))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()
plt.close()

# 4. Bar Chart (Average Charges by Region)
region_avg = df.groupby("region")["charges"].mean().reset_index()
plt.figure()
sns.barplot(x="region", y="charges", data=region_avg, palette="viridis")
plt.title("Average Charges by Region")
plt.tight_layout()
plt.show()
plt.close()

# 5. Scatter Plot (BMI vs Charges)
plt.figure()
sns.scatterplot(x="bmi", y="charges", hue="smoker", data=df, alpha=0.6)
plt.title("BMI vs Charges (Smoker VS Non-Smoker)")
plt.tight_layout()
plt.show()
plt.close()