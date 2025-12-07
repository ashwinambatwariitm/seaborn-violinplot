import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate realistic synthetic data for customer support response times
# Different support channels have different response time distributions

channels = []
response_times = []

# Email Support: Higher response times, wider distribution
email_times = np.random.gamma(shape=3, scale=45, size=150)
channels.extend(['Email'] * 150)
response_times.extend(email_times)

# Live Chat: Fast response times, narrow distribution
chat_times = np.random.gamma(shape=2, scale=8, size=150)
channels.extend(['Live Chat'] * 150)
response_times.extend(chat_times)

# Phone Support: Medium response times, moderate distribution
phone_times = np.random.gamma(shape=2.5, scale=20, size=150)
channels.extend(['Phone'] * 150)
response_times.extend(phone_times)

# Social Media: Variable response times, wide distribution
social_times = np.random.gamma(shape=2.8, scale=35, size=150)
channels.extend(['Social Media'] * 150)
response_times.extend(social_times)

# Create DataFrame
df = pd.DataFrame({
    'Channel': channels,
    'Response_Time_Minutes': response_times
})

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.9)

# Create figure with exact dimensions for 512x512 output
plt.figure(figsize=(8, 8))

# Create violinplot with professional styling
ax = sns.violinplot(
    data=df,
    x='Channel',
    y='Response_Time_Minutes',
    palette='Set2',
    inner='box',
    linewidth=1.5
)

# Customize the plot
plt.title('Customer Support Response Time Distribution by Channel', 
          fontsize=14, fontweight='bold', pad=20)
plt.xlabel('Support Channel', fontsize=12, fontweight='bold')
plt.ylabel('Response Time (Minutes)', fontsize=12, fontweight='bold')

# Rotate x-axis labels for better readability
plt.xticks(rotation=15, ha='right')

# Add grid for better readability
ax.yaxis.grid(True, alpha=0.3)
ax.set_axisbelow(True)

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save chart with exact 512x512 dimensions
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
print("Chart saved as 'chart.png' with 512x512 dimensions")

# Display the chart
plt.show()
