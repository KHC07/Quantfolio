# Portfolio Domain Model

## Purpose

The Portfolio class represents a collection of investment assets.

## Responsibilities

- Store Asset objects
- Add assets to the portfolio
- Calculate total portfolio cost basis

## Relationship with Asset

A Portfolio contains one or more Asset objects.

Each Asset is responsible for calculating its own cost basis. Portfolio aggregates these values to calculate the total cost basis.

## Current Limitations

The Portfolio does not currently:

- Retrieve market prices
- Calculate current market value
- Calculate returns
- Calculate risk metrics
- Perform portfolio optimization

These features will be introduced in later phases.