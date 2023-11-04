def can_buy(cost, balance=0):
    """Analize if you can afford something.

    This function is used to analize if you can afford a certain product.

    Args:_
        cost: the cost of the product.
        balance: the money that you have.

    Returns_
        bool(cost <= balance): boolean value indicating whether the balance is
                               enough to pay the cost.

    """
    return bool(cost <= balance)
