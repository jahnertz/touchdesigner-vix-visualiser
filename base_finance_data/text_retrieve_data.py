from yahoo_fin import stock_info

vix_current = stock_info.get_live_price("^VIX")

print ('{}'.format(vix_current))
op('table_vix')[0,0] = vix_current
