#%%
from prettytable import PrettyTable

#%%
raw_mat_OS = 12500
raw_mat_Purchases = 136000
raw_mat_CS = 8500
direct_wages = 54000
direct_expenses = 12000
factory_overheads = 100  #% of direct_wages
office_admin_overheads = 20  #% of works cost

selling_distrib_overheads = 26000
finished_goods_cost_OS = 12000
finished_goods_cost_CS = 15000

profit_on_cost = 20  #%
#%%
factory_overheads = factory_overheads * direct_wages // 100
#%%
# Units
selling_distrib_expenses = 3
in_hand = 500
produced = 12000
in_the_end = 1500
finished_goods_cost_OS = 12500

direct_material = raw_mat_Purchases + raw_mat_OS - raw_mat_CS
prime_cost = direct_material + direct_wages + direct_expenses

work_cost = prime_cost + factory_overheads


total_cost_per_unit = (
    work_cost + office_admin_overheads * work_cost // 100
) // produced
selling_distrib_overheads = selling_distrib_expenses * (produced + in_hand - in_the_end)
finished_goods_cost_CS = in_the_end * total_cost_per_unit
#%%
profit_on_cost = 100 * profit_on_cost / (100 - profit_on_cost)
#%%
direct_material = raw_mat_Purchases + raw_mat_OS - raw_mat_CS
prime_cost = direct_material + direct_wages + direct_expenses

work_cost = prime_cost + factory_overheads
office_admin_overheads = office_admin_overheads * work_cost // 100

total_cost_of_prod = office_admin_overheads + work_cost
cost_of_goods_sold = (
    finished_goods_cost_OS + total_cost_of_prod - finished_goods_cost_CS
)
total_cost = cost_of_goods_sold + selling_distrib_overheads
profit = total_cost * profit_on_cost // 100
sales = total_cost + profit


tab = PrettyTable()
tab.field_names = ["Particulars", "Ammount1", "Ammount"]
tab.align["Particulars"] = "l"
tab.add_row(["Opening Stock of raw materials", raw_mat_OS, ""])
tab.add_row(["Add: Purchases of raw materials", raw_mat_Purchases, ""])
tab.add_row(["", "------", ""])
tab.add_row(["Material available for consumption", raw_mat_Purchases + raw_mat_OS, ""])

tab.add_row(["Less: Closing Stock of raw materials", f"({raw_mat_CS})", ""])

tab.add_row(["", "------", ""])
tab.add_row(["Material consumed", direct_material, ""])

tab.add_row(["Add: Direct wages", direct_wages, ""])
tab.add_row(["Add: Direct expenses", direct_expenses, ""])

tab.add_row(["", "------", "------"])

tab.add_row(["                          PRIME COST", "", prime_cost])


tab.add_row(["Add: Factory overheads", "", factory_overheads])

tab.add_row(["", "", "------"])

tab.add_row(["                          WORK COST", "", work_cost])


tab.add_row(["Add: Office Admin overheads", "", office_admin_overheads])

tab.add_row(["", "", "------"])

tab.add_row(["              TOTAL COST OF PRODUCTION", "", total_cost_of_prod])

tab.add_row(["Add: Opening Stock of finished goods", "", finished_goods_cost_OS])
tab.add_row(["", "", "------"])
tab.add_row(
    [
        "Cost of goods available for sale",
        "",
        finished_goods_cost_OS + total_cost_of_prod,
    ]
)
tab.add_row(
    ["Less: Closing Stock of finished goods", "", f"({finished_goods_cost_CS})"]
)

tab.add_row(["", "", "------"])

tab.add_row(["                   COST OF GOODS SOLD", "", cost_of_goods_sold])

tab.add_row(["Add: Selling and distribution overheads", "", selling_distrib_overheads])

tab.add_row(["", "", "------"])

tab.add_row(["                          TOTAL COST", "", total_cost])


tab.add_row(["Add: Profit", "", profit])

tab.add_row(["", "", "------"])

tab.add_row(["                          SALES", "", sales])
tab.add_row(["", "", "======"])
#%%
print(tab)
#%%
raw_mat_OS = 20000
raw_mat_Purchases = 122000
raw_mat_CS = 10000
direct_wages = 36000
direct_expenses = 24000
factory_overheads = 50  #% of direct_wages
factory_overheads = factory_overheads * direct_wages // 100
office_admin_overheads = 20  #% of works cost


profit_on_cost = 20  #%on sale
profit_on_cost = 100 * profit_on_cost / (100 - profit_on_cost)
#%%
raw_mat_OS = 00
raw_mat_Purchases = 160000
raw_mat_CS = 00
direct_wages = 45000
direct_expenses = 15000
factory_overheads = 35000  #% of direct_wages
office_admin_overheads = 20  #% of works cost

selling_distrib_overheads = 45000
finished_goods_cost_OS = 25000
finished_goods_cost_CS = 10000

profit_on_cost = 11.2  #%
#%%
raw_mat_OS = 62500
raw_mat_Purchases = 100000
raw_mat_CS = 8500
direct_wages = 54000
direct_expenses = 12000
factory_overheads = 50  #% of direct_wages
office_admin_overheads = 10  #% of works cost

selling_distrib_overheads = 26000
finished_goods_cost_OS = 12000
finished_goods_cost_CS = 15000

profit_on_cost = 20  #%
# %%
