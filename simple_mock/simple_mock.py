import mock
class SimpleMockException(Exception):
    """ Exception to raise in Simple Mock"""
    pass


class SimpleMock(object):
    def __init__(self):
        self.patched_func_list = []

    def patch_func(self, func, exptd_ret_val=None,
                   exptd_err=None, err_msg="exception through mock"):
        """
        :param func:
        :param exptd_ret_val:
        :param exptd_err:
        :param err_msg:
        :return:
        """

        func = ".".join(["__main__", func])
        mock_func = None
        if not (exptd_ret_val or exptd_err) or (exptd_ret_val and exptd_err):
            raise ValueError("either return_value or return error expected")
        if exptd_ret_val:
            mock_func = mock.Mock(return_value=exptd_ret_val)
        elif exptd_err:
            mock_func = mock.Mock(side_effect=exptd_err(err_msg))
        else:
            pass

        patched_func = mock.patch(func, mock_func)
        # start patch effect immediately
        self.start(patched_func)
        return patched_func

    def start(self, patched_func):
        """
        :param patched_func:
        :return:
        """
        try:
            patched_func.start()
            self.patched_func_list.append(patched_func)
        except ImportError as ie:
            raise SimpleMockException(ie.message + ". Incorrect function path passed for mocking")

    def stop(self, patched_func):
        """
        :param patched_func:
        :return:
        """
        try:
            patched_func.stop()
            self.patched_func_list.remove(patched_func)
        except RuntimeError as re:
            print("stop called on unstarted func - {}".format(patched_func))

    def clear_all_patch(self):
        """
        :return:
        """
        for patch_func in self.patched_func_list:
            self.stop(patch_func)

    def get_all_patched_fun(self):
        """
        :return:
        """
        print("Patched functions list :: {}".format(self.patched_func_list))
