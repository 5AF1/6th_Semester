#%%
from prettytable import PrettyTable

#%%
class CVP:
    def __init__(self, speakers, sales_pu, var_exp_pu, fix_exp, target_profit):
        self.sales_pu = sales_pu
        self.speakers = speakers
        self.var_exp_pu = var_exp_pu
        self.fix_exp = fix_exp
        self.target_profit = target_profit

    def sales(self):
        return self.sales_pu * self.speakers

    def var_exp(self):
        return self.var_exp_pu * self.speakers

    def contrib_margin_d(self):
        return self.sales() - self.var_exp()

    def contrib_margin_pu(self):
        return self.contrib_margin_d() / self.speakers

    def contrib_margin_rat(self):
        return self.contrib_margin_d() / self.sales()

    def var_exp_rat(self):
        return self.var_exp() / self.sales()

    def net_op_income(self):
        return self.contrib_margin_d() - self.fix_exp

    def break_even_pt_u(self):
        return self.fix_exp / self.contrib_margin_pu()

    def break_even_pt_d(self):
        return self.fix_exp / self.contrib_margin_rat()

    def u_sales_target_profit(self):
        return (self.fix_exp + self.target_profit) / self.contrib_margin_pu()

    def d_sales_target_profit(self):
        return (self.fix_exp + self.target_profit) / self.contrib_margin_rat()

    def marginal_safety(self):
        return self.sales() - self.break_even_pt_d()

    def marginal_safety_p(self):
        return self.marginal_safety() / self.sales()

    def degree_operating_leverage(self):
        return self.contrib_margin_d() / self.net_op_income()

    def expected_inc_in_net_op_inc(self, expected_inc_in_sale):
        print(f"Expected increase in sales\t{expected_inc_in_sale}")
        print(f"Degree of operating leverage\t{self.degree_operating_leverage()}")
        print(
            f"Expected increase in net operating income \t{self.degree_operating_leverage() * expected_inc_in_sale}"
        )
        return self.degree_operating_leverage() * expected_inc_in_sale

    def table(self):
        tab = PrettyTable()
        tab.field_names = ["", "Total", "Per Unit"]
        tab.align[""] = "l"
        tab.add_row(
            [f"Sales ({self.speakers} Units)", f"${self.sales()}", f"${self.sales_pu}"]
        )
        tab.add_row(
            [f"Less: Variable Expenses", f"({self.var_exp()})", f"({self.var_exp_pu})"]
        )
        tab.add_row([f"", "-----", "-----"])
        tab.add_row(
            [
                f"Contribution Margin",
                f"{self.contrib_margin_d()}",
                f"${self.contrib_margin_pu()}",
            ]
        )
        tab.add_row([f"Less: Fixed Expenses", f"({self.fix_exp})", "====="])
        tab.add_row([f"", "-----", ""])
        tab.add_row([f"Net Operating Income", f"${self.net_op_income()}", ""])
        tab.add_row([f"", "=====", ""])

        print(tab)


#%%
#%%
a = CVP(400, 250, 150, 35000, None)
a.table()
#%%
a.degree_operating_leverage()
#%%
a.speakers = int(a.speakers * 1.1)
a.var_exp_pu += 10
a.fix_exp -= 5000
a.table()
#%%
a = CVP(20000, 60, 45, 240000, 90000)
a.table()
print(a.contrib_margin_rat(), a.var_exp_rat())
print(a.break_even_pt_d(), a.break_even_pt_u())
print(a.d_sales_target_profit(), a.u_sales_target_profit())
print(a.marginal_safety(), a.marginal_safety_p())
print(a.expected_inc_in_net_op_inc(8))
#%%
a = CVP(20000, 60, 45, 240000, 90000)
a.table()
a.var_exp_pu += 3
a.fix_exp -= 30000
a.speakers *= 1.2
a.table()
#%%
a = CVP(2000, 90, 63, 30000, None)
a.table()

a.sales_pu *= 1.05
a.var_exp_pu *= 1.05
a.fix_exp += 5000
a.table()

a = CVP(2000, 90, 63, 30000, None)

a.var_exp_pu += 2
a.speakers *= 1.1
a.table()
#%%
if __name__ == "__main__":
    a = CVP(400, 250, 150, 35000, None)
    a.table()
    print(a.degree_operating_leverage())
#%%
a = CVP(30000, 50, 35, 300000, None)
a.table()

# %%
