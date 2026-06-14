import pandas as pd
import matplotlib.pyplot as plt

#reading the data
df=pd.read_excel("CleanedData.xlsx")
data=df[~((df["OrderStatus"]=="Cancelled") | (df["OrderStatus"]=="Returned"))]
print(data.head())
print("Columns in the cleaned data are : ",data.columns)


#color coding to highlight particular bar
def get_color(index_values, highlight_value):
    colors=[]
    for i in index_values:
        if i==highlight_value:
            colors.append("blue")
        else:
            colors.append("lightgray")
    return colors


#Data Visualisation
pdt_quantity=data.groupby("Product")["Quantity"].sum()
colors=get_color(pdt_quantity.index, "Chair")
pdt_quantity.plot(kind="bar", color=colors)
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.title("Chair Drove the Highest Product Demand")
plt.tight_layout()
plt.show()


pymt_method=data["PaymentMethod"].value_counts()
colors=get_color(pymt_method.index,"Online")
pymt_method.plot(kind="pie",autopct="%1.1f%%", colors=colors)
plt.title("Customers Preferred Online Methods for Purchases")
plt.tight_layout()
plt.show()


order_status=df["OrderStatus"].value_counts()
colors=get_color(order_status.index,"Cancelled")
order_status.plot(kind="barh", color=colors)
plt.title("Order Cancellation Dominated Overall Order Outcomes")
plt.xlabel("Count")
plt.ylabel("Order Status")
plt.tight_layout()
plt.show()

loss_revenue = (
    df[(df["OrderStatus"] == "Cancelled") | (df["OrderStatus"] == "Returned")]
    .groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)
colors = ["lightgray"] * len(loss_revenue)
colors[0] = "blue"  
loss_revenue.plot(kind="bar", color=colors)
plt.title("Laptop Contributed the Highest Revenue Loss when orders are Cancelled or Retuned")
plt.xlabel("Product")
plt.ylabel("Lost Revenue")
plt.tight_layout()
plt.show()

revenue = (
    data.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
)
colors = ["lightgray"] * len(revenue)
colors[0] = "blue"     # highest revenue product
revenue.plot(kind="bar", color=colors)
plt.title("Printer Led Revenue Generation After Excluding Cancelled and Returned Orders")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()


coupon_code=data["CouponCode"].value_counts()
colors=get_color(coupon_code.index,"FREESHIP")
coupon_code.plot(kind="bar", color=colors)
plt.title("Customers Strongly Preferred the FREESHIP Discount Offer in Successful Orders")
plt.xlabel("Coupon Code")
plt.ylabel("Count")
plt.tight_layout()
plt.show()


referral_source=data["ReferralSource"].value_counts()
colors=get_color(referral_source.index,"Instagram")
referral_source.plot(kind="barh", color=colors)
plt.xlabel("Count")
plt.ylabel("Referral Source")
plt.title("Instagram Generated the Highest Customer Traffic & Successful Orders")
plt.tight_layout()
plt.show()

data["Month"] = data["Date"].dt.to_period("M")
data.groupby("Month")["TotalPrice"].sum().plot(kind="line", marker="o")
plt.title("Sales Performance Varied Significantly Across Months")
plt.ylabel("Total Price")
plt.xlabel("Months")
plt.tight_layout()
plt.show()