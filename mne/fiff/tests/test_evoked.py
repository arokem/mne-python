import os
import os.path as op

from numpy.testing import assert_array_almost_equal, assert_equal

from .. import read_evoked, write_evoked

fname = op.join(op.dirname(__file__), 'data', 'test-ave.fif')

def test_io_evoked():
    """Test IO for noise covariance matrices
    """
    data = read_evoked(fname)

    write_evoked('evoked.fif', data)
    data2 = read_evoked('evoked.fif')

    print assert_array_almost_equal(data['evoked']['epochs'],
                                    data2['evoked']['epochs'])
    print assert_array_almost_equal(data['evoked']['times'],
                                    data2['evoked']['times'])
    print assert_equal(data['evoked']['nave'],
                                    data2['evoked']['nave'])
    print assert_equal(data['evoked']['aspect_kind'],
                                    data2['evoked']['aspect_kind'])
    print assert_equal(data['evoked']['last'],
                                    data2['evoked']['last'])
    print assert_equal(data['evoked']['first'],
                                    data2['evoked']['first'])
