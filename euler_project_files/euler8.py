"""
Time Complexity: O(mk), where m is the number of digits and k is the window size
Space Complexity: O(m)
"""


def largest_product_in_a_series(n, k):
    digits = [int(d) for d in str(n)]
    max_product = 0
    for i in range(len(digits) - k + 1):
        product = 1
        for j in range(k):
            product *= digits[i + j]
        if product > max_product:
            max_product = product
    return max_product


print(largest_product_in_a_series(731671765313306249192251196744265747423553491949349698352031277450632623957831801698480186947885184385861560789112949495459501737958331952853208805511125406987471585238630507156932909632952274430435576689664895044524435216173185640309871112172238311362229893423380305861786645835912456652947654568284891288314206907002421902, 13))
