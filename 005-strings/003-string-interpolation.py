open_, high, low, close = 98, 100, 95, 99

print("open: " + str(open_) + ", high: " + str(high) + ", low: " + str(low) + ", close: " + str(close))
print("open: {}, high: {}, low: {}, close: {}".format(open_, high, low, close))

bid = 1.5760
ask = 1.5763
print("bid: {}, ask: {}, spread: {}".format(bid, ask, ask-bid))
print("bid: {b}, ask: {a}, spread: {spread}".format(a=ask, b=bid, spread=ask-bid))
print("bid: {:.4f}, ask: {:.4f}, spread: {:.4f}".format(bid, ask, ask-bid))
print("bid: {b:.4f}, ask: {a:.4f}, spread: {spread:.4f}".format(a=ask, b=bid, spread=ask-bid))
print(f"bid: {bid:.4f}, ask: {ask: .4f}, spread: {ask-bid:.4f}")
bid = 100
print(f"bid: {bid:.4f}, ask: {ask: .4f}, spread: {ask-bid:.4f}")