from tsetmc_api.symbol import Symbol
import time 
import math



symbol = Symbol(symbol_id='14079693677610396')

price_overview = symbol.get_price_overview().traders_type
real_buy_count_p =price_overview.real.buy.count
real_buy_vol_p=price_overview.real.buy.volume

price_data=symbol.get_price_overview().price_data
last_price_p=price_data.last
#print(var1)

time.sleep(1)

price_overview = symbol.get_price_overview().traders_type
real_buy_count =price_overview.real.buy.count
real_buy_vol=price_overview.real.sell.volume

price_data=symbol.get_price_overview().price_data
last_price=price_data.last




real_buy_value = round(((real_buy_vol - real_buy_vol_p) * (last_price+last_price_p /2)) / 10000000)
dif_real_buy_count = real_buy_count - real_buy_count_p
each_dif_real_buy_value = real_buy_value / dif_real_buy_count

if dif_real_buy_count > 0:
    if each_dif_real_buy_value >= 500 or (each_dif_real_buy_value >= 300 and dif_real_buy_count >= 5):
        if sessionStorage.getItem("kh_hagh_counter = " + l18) == None:
            sessionStorage.setItem("kh_hagh_counter = " + l18, 1)

        sessionStorage.setItem("code_be_cod_hagh_kh = " + l18, saat)

        counter_kh = int(sessionStorage.getItem("kh_hagh_counter = " + l18))
        for i in range(0, len(dafe), 2):
            if counter_kh == dafe[i]:
                dafe_kh = dafe[i + 1]

        if each_dif_real_buy_value > 1000:
            each_dif_real_buy_value = str(round(each_dif_real_buy_value / 100) / 10) + ' میلیارد تومان '
        else:
            each_dif_real_buy_value = str(round(each_dif_real_buy_value)) + ' میلیون تومان '

        telgeramMsg = (
            "\n"
            + "#" + l18.replace(" ", "_") + " 🟢 " + "#" + dafe_kh + "_" + "خرید" + "_" + "حقیقی".bold() + " 👨‍💼 "
            + "\n" + str(dif_real_buy_count) + ' نفر هر کد ' + each_dif_real_buy_value + " در " + "%" + plp
            + "\n" + ghodrat_emo + ' قدرت : ' + ghodrat_p + "👈" + ghodrat + ghodrat_taghir_emo
            + "\n" + vrod_pool
            + "\n" + "⏰ " + ntime
        )
        Kharid_Gorohi(encodeURIComponent(telgeramMsg))
        counter_kh += 1
        sessionStorage.setItem("kh_hagh_counter = " + l18, counter_kh)
