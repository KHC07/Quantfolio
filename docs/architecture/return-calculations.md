# Return Calculations Architecture

## Purpose

The return analytics layer calculates different measures of investment performance from historical price data.

## Return Calculations

The module currently provides:

- Periodic Returns
- Cumulative Returns
- Total Return
- Annualized Return
- Log Returns

## Data Flow

Historical prices are provided to the return calculation functions.

```text
Historical Prices
       ↓
Return Calculations
       ↓
Performance Metrics