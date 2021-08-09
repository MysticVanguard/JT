from pandas.core.base import NoNewAttributesMixin as NoNewAttributesMixin
from pandas.core.series import Series
from typing import List

def cat_core(list_of_columns: List, sep: str) : ...
def cat_safe(list_of_columns: List, sep: str) : ...
def str_count(arr, pat, flags: int = ...): ...
def str_contains(arr, pat, case: bool = ..., flags: int = ..., na = ..., regex: bool = ...): ...
def str_startswith(arr, pat, na = ...): ...
def str_endswith(arr, pat, na = ...): ...
def str_replace(arr, pat, repl, n: int = ..., case = ..., flags: int = ..., regex: bool = ...): ...
def str_repeat(arr, repeats): ...
def str_match(arr, pat, case: bool = ..., flags: int = ..., na = ...): ...
def str_extract(arr, pat, flags: int = ..., expand: bool = ...): ...
def str_extractall(arr, pat, flags: int = ...): ...
def str_get_dummies(arr, sep: str = ...): ...
def str_join(arr, sep): ...
def str_findall(arr, pat, flags: int = ...): ...
def str_find(arr, sub, start: int = ..., end = ..., side: str = ...): ...
def str_index(arr, sub, start: int = ..., end = ..., side: str = ...): ...
def str_pad(arr, width, side: str = ..., fillchar: str = ...): ...
def str_split(arr, pat = ..., n = ...): ...
def str_rsplit(arr, pat = ..., n = ...): ...
def str_slice(arr, start = ..., stop = ..., step = ...): ...
def str_slice_replace(arr, start = ..., stop = ..., repl = ...): ...
def str_strip(arr, to_strip = ..., side: str = ...): ...
def str_wrap(arr, width, **kwargs): ...
def str_translate(arr, table): ...
def str_get(arr, i): ...
def str_decode(arr, encoding, errors: str = ...): ...
def str_encode(arr, encoding, errors: str = ...): ...
def forbid_nonstring_types(forbidden, name = ...): ...
def copy(source): ...

class StringMethods(NoNewAttributesMixin):
    def __init__(self, data) -> None: ...
    def __getitem__(self, key): ...
    def __iter__(self) : ...
    def cat(self, others = ..., sep = ..., na_rep = ..., join: str = ...): ...
    def split(self, pat = ..., n: int = ..., expand: bool = ...): ...
    def rsplit(self, pat = ..., n: int = ..., expand: bool = ...): ...
    def partition(self, sep: str = ..., expand: bool = ...): ...
    def rpartition(self, sep: str = ..., expand: bool = ...): ...
    def get(self, i): ...
    def join(self, sep): ...
    def contains(self, pat, case: bool = ..., flags: int = ..., na = ..., regex: bool = ...) -> Series[bool]: ...
    def match(self, pat, case: bool = ..., flags: int = ..., na = ...): ...
    def replace(self, pat, repl, n: int = ..., case = ..., flags: int = ..., regex: bool = ...): ...
    def repeat(self, repeats): ...
    def pad(self, width, side: str = ..., fillchar: str = ...): ...
    def center(self, width, fillchar: str = ...): ...
    def ljust(self, width, fillchar: str = ...): ...
    def rjust(self, width, fillchar: str = ...): ...
    def zfill(self, width): ...
    def slice(self, start = ..., stop = ..., step = ...): ...
    def slice_replace(self, start = ..., stop = ..., repl = ...): ...
    def decode(self, encoding, errors: str = ...): ...
    def encode(self, encoding, errors: str = ...): ...
    def strip(self, to_strip = ...): ...
    def lstrip(self, to_strip = ...): ...
    def rstrip(self, to_strip = ...): ...
    def wrap(self, width, **kwargs): ...
    def get_dummies(self, sep: str = ...): ...
    def translate(self, table): ...
    count = ...
    startswith = ...
    endswith = ...
    findall = ...
    def extract(self, pat, flags: int = ..., expand: bool = ...): ...
    def extractall(self, pat, flags: int = ...): ...
    def find(self, sub, start: int = ..., end = ...): ...
    def rfind(self, sub, start: int = ..., end = ...): ...
    def normalize(self, form): ...
    def index(self, sub, start: int = ..., end = ...): ...
    def rindex(self, sub, start: int = ..., end = ...): ...
    len = ...
    lower = ...
    upper = ...
    title = ...
    capitalize = ...
    swapcase = ...
    casefold = ...
    isalnum = ...
    isalpha = ...
    isdigit = ...
    isspace = ...
    islower = ...
    isupper = ...
    istitle = ...
    isnumeric = ...
    isdecimal = ...

