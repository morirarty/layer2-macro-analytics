-- =========================================================================
-- Query Name: Layer 2 Macro Economics - Base Network Growth
-- Description: Tracks Daily Active Users (DAU), Transaction Volume, and 
--              Network Revenue (Gas Fees) on the Base L2 Network.
-- =========================================================================

SELECT 
    DATE_TRUNC('day', block_time) AS transaction_date,
    COUNT(DISTINCT "from") AS daily_active_users,
    COUNT(hash) AS total_daily_transactions,
    -- Calculate total transaction fees (Network Revenue) in ETH
    -- Formula: (gas_used * gas_price) divided by 1e18 for decimal conversion
    SUM(gas_used * gas_price) / 1e18 AS total_network_revenue_eth
FROM base.transactions
WHERE block_time >= NOW() - INTERVAL '30' DAY
  -- Filter to ensure we only count successful transactions
  AND success = true 
GROUP BY 1
ORDER BY 1 DESC;