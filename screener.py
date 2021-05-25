    # fig, ax = plt.subplots(nrows=2)
    # # ax.plot(data.index, data.wma9, label='wma9')
    # # ax.plot(data.index, data.wma18, label='wma18')
    # # ax.plot(data.index, data.wma100, label='wma100')
    # ax[0].set_title(symbol)
    # ax[0].plot(data.index, data.RSI, label='rsi')
    # ax[1].plot(data.index, data.Close,
    #            label='close price'+symbol)
    # ax[1].plot(data.index, data.wma18,
    #            label='wma18'+symbol)
    # ax[1].plot(data.index, data.wma9,
    #            label='wma9'+symbol)
    # # ax[1].plot(data.index, data.wma100,
    # # label = 'wma100'+symbol)
    # for idx, row in data.iterrows():
    #     rango = data.Close.max()-data.Close.min()
    #     h = (row.Close-data.Close.min())/rango

    #     if row.EMAssignal == -1.00:
    #         ax[1].axvline(x=idx, ymin=0, ymax=h,
    #                       c='red', ls='--')
    #     if row.EMAssignal == 1.00:
    #         ax[1].axvline(x=idx, ymin=0, ymax=h,
    #                       c='green', ls='solid')
    # plt.show()


