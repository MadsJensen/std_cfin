def rms(epochs, chan_type="grad"):
    """

    :param epochs:
    :param ch_type:
    :return:
        rms : Evoked
        rms_line = array
    """
    epo = epochs.copy()
    epo.load_data()
    epo.pick_types(meg=chan_type)
    evoked = epo.average()
    evoked_rms = evoked.copy()
    evoked_rms._data = evoked._data ** 2

    rms_line = evoked_rms._data.mean(axis=0)
    return evoked_rms, rms_line