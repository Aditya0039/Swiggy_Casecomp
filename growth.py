import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
initial_users = 2749.0
SAM = 11550.0
s_curve_annual_growth_rates = [0.10, 0.25, 0.35, 0.20, 0.10]
years_list = list(range(6))
total_users_list = [initial_users]
new_users_gained_list = [0]
growth_rate_list = [0.0]
current_users = initial_users
for rate in s_curve_annual_growth_rates:
    new_users_this_year = current_users * rate
    current_users += new_users_this_year
    total_users_list.append(current_users)
    new_users_gained_list.append(new_users_this_year)
    growth_rate_list.append(rate)
df = pd.DataFrame({
    'Year': years_list,
    'Annual_Growth_Rate_Percent': [r * 100 for r in growth_rate_list],
    'New_Users_This_Year': new_users_gained_list,
    'Total_Predicted_Users': total_users_list
})
df['New_Users_This_Year'] = df['New_Users_This_Year'].round(0).astype(int)
df['Total_Predicted_Users'] = df['Total_Predicted_Users'].round(0).astype(int)
print("Projected S-Curve (Compounding Growth) Data:\n",
      df.to_markdown(index=False))
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Total_Predicted_Users'], marker='o',
         linestyle='-', color='purple', label='Total Predicted Users (S-Curve)')
for i, row in df.iterrows():
    plt.text(row['Year'], row['Total_Predicted_Users'] + 60,
             f"{row['Total_Predicted_Users']}", ha='center', fontsize=10)

plt.title('Predicted 5-Year S-Curve (Compounding) User Growth', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Total Predicted Swiggy Users', fontsize=12)
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
plt.ylim(bottom=df['Total_Predicted_Users'].min() * 0.98)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
image_path = 'swiggy_user_growth_s_curve_compounding.png'
plt.savefig(image_path)
print(f"\nStatic S-Curve image plot saved to {image_path}")
