from telebot import types




markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('a')
itembtn2 = types.KeyboardButton('v')
itembtn3 = types.KeyboardButton('d')


markup = types.ReplyKeyboardMarkup()
itembtna = types.KeyboardButton('a')
itembtnv = types.KeyboardButton('v')
itembtnc = types.KeyboardButton('c')
itembtnd = types.KeyboardButton('d')
itembtne = types.KeyboardButton('e')
markup.row(itembtna, itembtnv)
markup.row(itembtnc, itembtnd, itembtne)



markup = types.ReplyKeyboardRemove(selective=False)


markup = types.ForceReply(selective=False)


markup = types.ForceReply(selective=False)


markup = types.ReplyKeyboardRemove(selective=False)

markup = types.ForceReply(selective=False)
