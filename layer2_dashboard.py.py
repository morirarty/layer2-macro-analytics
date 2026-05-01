# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "dune-client==1.10.0",
#     "marimo>=0.23.4",
#     "matplotlib==3.10.8",
#     "pandas==3.0.2",
# ]
# ///

import marimo

__generated_with = "0.23.0"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    from dune_client.client import DuneClient

    # ==========================================
    # 1. DUNE API CONFIGURATION
    # ==========================================
    # Replace with your API Key and Dune Analytics Query ID
    DUNE_API_KEY = "iEuaSNBZeMLZcwoqQdAqWa1uVUgyQ8d3"
    QUERY_ID = 7411975  # Replace with your Base L2 Macro-Economics Query ID

    print("Fetching data from Dune Analytics server...")
    dune = DuneClient(DUNE_API_KEY)
    result = dune.get_latest_result(QUERY_ID)

    # Convert raw data into a Pandas DataFrame
    df = pd.DataFrame(result.result.rows)

    # ==========================================
    # 2. DATA WRANGLING
    # ==========================================
    # Ensure the date column is properly read as datetime format
    df['transaction_date'] = pd.to_datetime(df['transaction_date'])
    # Sort data from oldest to newest
    df = df.sort_values('transaction_date')

    # ==========================================
    # 3. DATA VISUALIZATION (DUAL-AXIS CHART)
    # ==========================================
    print("Building dashboard visualization...")

    # Set canvas size (12x6 inches)
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # --- Left Axis (Active Users) ---
    color_users = 'tab:blue'
    ax1.set_xlabel('Date', fontweight='bold')
    ax1.set_ylabel('Daily Active Users (DAU)', color=color_users, fontweight='bold')
    # Draw thick line with markers
    ax1.plot(df['transaction_date'], df['daily_active_users'], color=color_users, linewidth=2.5, marker='o', label='Daily Active Users')
    ax1.tick_params(axis='y', labelcolor=color_users)
    ax1.grid(True, linestyle='--', alpha=0.5)

    # --- Right Axis (ETH Revenue) ---
    # .twinx() creates a second Y-axis on the right side
    ax2 = ax1.twinx()  
    color_revenue = 'tab:green'
    ax2.set_ylabel('Network Revenue (ETH)', color=color_revenue, fontweight='bold')
    # Draw thin bar chart in the background to avoid hiding the main line
    ax2.bar(df['transaction_date'], df['total_network_revenue_eth'], color=color_revenue, alpha=0.3, label='Network Revenue (ETH)')
    ax2.tick_params(axis='y', labelcolor=color_revenue)

    # --- Formatting and Cleanup ---
    plt.title('Base L2 Network: User Growth vs Network Revenue (Last 30 Days)', fontsize=14, fontweight='bold', pad=20)
    fig.autofmt_xdate() # Slant the dates to prevent overlap

    # Save final result as high-resolution image
    plt.savefig('base_l2_macro_dashboard.png', dpi=300, bbox_inches='tight')
    print("Success! Image saved as 'base_l2_macro_dashboard.png'")

    # Display image on screen
    plt.show()
    return


if __name__ == "__main__":
    app.run()
