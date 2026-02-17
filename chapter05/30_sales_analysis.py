

def main():
    months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December']    
    
    sales = [12_000, 14_500, 13_200, 15_000, 20_000, 18_500,
             16_000, 15_500, 14_000, 19_000, 22_500, 24_000]
    
    monthly_sales = dict(zip(months, sales))
    print(monthly_sales)

    for month, sales in monthly_sales.items():
        print(f"{month:<9}: {sales:>6}")

    print("-" * 30)
    high_monthly_sales = {month: sales for month, sales in monthly_sales.items() if sales > 17000}
    for month, sales in high_monthly_sales.items():
        print(f"{month:<9}: {sales:>6}")    

    # discount 10%
    discounted_sales = { month: sales * 0.9 if sales > 20_000 else sales 
                        for month, sales in monthly_sales.items()
    }
    for month, sales in discounted_sales.items():
        print(f"{month:<9}: {sales:>6}")


    discounted_sales = { month: sales * 0.9 for month, sales in monthly_sales.items() 
                        if sales > 20_000 
    }
    print(discounted_sales)

    # Total sales
    total_sales = sum(monthly_sales.values())
    print(f"Total sales: {total_sales}")

    # vat

    # best month
    best_month = max(monthly_sales, key=monthly_sales.get)
    print(f"Best month: {best_month} with sales: {monthly_sales[best_month]}")

    # worst month
    worst_month = min(monthly_sales, key=monthly_sales.get)
    print(f"Worst month: {worst_month} with sales: {monthly_sales[worst_month]}")

if __name__ == "__main__":
    main()   