# ------------------------------------------------------------------------------
# Copyright (C) 2022-2023 M. Colange

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# ------------------------------------------------------------------------------

from typing import Union, Any, List
from pandas import Categorical


class Factor(Categorical):
    """
    A class to represent a factor, as in R.

    It is essentially a :obj:`pandas.Categorical` object, with additional
    methods to mimic R API.
    """

    def __init__(self, arr: Union[List[Any], tuple, 'Factor']) -> None:
        """
        Constructs a Factor instance from an array

        Arguments
        ---------
        arr : array_like
            a list of factors
        """

        super().__init__(arr)

    def droplevels(self) -> 'Factor':
        """
        Drop unused levels

        Returns
        -------
        Factor
            a new Factor object with unused levels removed
        """

        return Factor(self.__array__())

    def nlevels(self) -> int:
        """
        Get the number of levels

        Returns
        -------
        int
            the number of levels
        """

        return len(self.categories)


def asfactor(g: Union[List[Any], tuple, 'Factor']) -> 'Factor':
    """
    Convert an array-like object to a Factor

    Parameters
    ----------
    g : array_like
        The object to convert to a Factor

    Returns
    -------
    Factor
        A Factor object based on the input
    """
    if type(g) is Factor:
        return g
    else:
        return Factor(g)


def gl(n: int, k: int) -> 'Factor':
    """
    Generate factor levels

    Parameters
    ----------
    n : int
        The number of levels
    k : int
        The number of replications for each level

    Returns
    -------
    Factor
        A Factor object with generated levels
    """
    arr = []
    for i in range(1, n + 1):
        arr.extend([i for j in range(k)])
    return Factor(arr)