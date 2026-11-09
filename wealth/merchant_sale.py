# ------------------------------------------------------------------------
#
#  Function: merchant_sale
#
#  Inputs: gold (integer)
#  Returns: gold (integer)
#
#  Description: Player earns gold by selling goods at a market.
#
#  Author: <Aidan Preston>
#
# ------------------------------------------------------------------------

import random

def merchant_sale(gold):
    sale = random.randint(5, 20)

    print("A traveler stops by your market stall.")
    print(f"You sell some goods and earn {sale} gold!")

    return gold + sale
