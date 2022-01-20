from scipy.spatial import ConvexHull as qhull
import numpy as np
import itertools
import cdd #Install via "pip install pycddlib"


def chull1(mat):
    return np.asarray(qhull(mat, qhull_options='QJ').simplices)


def cddMatrix_to_npArray(cddmat):
    # return np.array(list((cddmat.__getitem__(i) for i in range(cddmat.row_size))))
    return np.fromiter(itertools.chain.from_iterable((cddmat.__getitem__(i) for i in range(cddmat.row_size))), dtype=int).reshape((cddmat.row_size, -1))

def chull2(mat):
    cddmat = cdd.Matrix(mat, number_type='fraction')
    cddmat.rep_type = cdd.RepType.INEQUALITY
    return cddMatrix_to_npArray(cdd.Polyhedron(cddmat).get_generators())

def chull3(mat):
    cddmat = cdd.Matrix(mat, number_type='fraction')
    cddmat.rep_type = cdd.RepType.GENERATOR
    return cddMatrix_to_npArray(cdd.Polyhedron(cddmat).get_inequalities())




if __name__ == '__main__':
    test = np.asarray([[1, 0, 1],
            [0, 1, 1],
            [-1, 0, 1],
            [0, -1, 1]])


    print(chull1(test))
    print(chull2(test))
    print(chull3(test))
#
#
#
#
# mat = cdd.Matrix(test, number_type='fraction')
# mat.rep_type = cdd.RepType.INEQUALITY
# poly = cdd.Polyhedron(mat)
# ext = poly.get_generators()
# print(cddMatrix_to_npArray(ext))
#
# mat = cdd.Matrix(test, number_type='fraction')
# mat.rep_type = cdd.RepType.GENERATOR
# poly = cdd.Polyhedron(mat)
# ext = poly.get_inequalities()
# print(cddMatrix_to_npArray(ext))
#
#
#
# # extracted_mat = np.fromiter(itertools.chain.from_iterable((ext.__getitem__(i) for i in range(ext.row_size))), dtype=int).reshape((ext.row_size, ext.col_size))
#
#

