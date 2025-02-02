from fastapi import FastAPI, Query
import json

app = FastAPI()

# Load student marks from the provided JSON file
data = [
    {"name": "nBzonNey", "marks": 3},
    {"name": "tx", "marks": 58},
    {"name": "6", "marks": 45},
    {"name": "xXMgTAaT5o", "marks": 65},
    {"name": "wtMY6s", "marks": 76},
    {"name": "S", "marks": 29},
    {"name": "kqPbl", "marks": 81},
    {"name": "7YJVUWilN7", "marks": 16},
    {"name": "6", "marks": 63},
    {"name": "b6cGbIIs3", "marks": 83},
    {"name": "M", "marks": 98},
    {"name": "OT0qKh8", "marks": 49},
    {"name": "VwzAh", "marks": 56},
    {"name": "zlLPitYq", "marks": 64},
    {"name": "Bqb", "marks": 93},
    {"name": "HKEqyoUQv", "marks": 1},
    {"name": "ea5E", "marks": 78},
    {"name": "qg1tRk", "marks": 2},
    {"name": "5aGvA7rEq", "marks": 84},
    {"name": "5beI48K0", "marks": 93},
    {"name": "Y", "marks": 43},
    {"name": "GDbzT", "marks": 4},
    {"name": "oT", "marks": 9},
    {"name": "m1PvFP4bU", "marks": 62},
    {"name": "CNp1vn", "marks": 98},
    {"name": "ZhNh", "marks": 99},
    {"name": "6NrGj", "marks": 30},
    {"name": "mzAEPqL9Y9", "marks": 0},
    {"name": "C", "marks": 46},
    {"name": "8iE1", "marks": 83},
    {"name": "F5pAtRp4x", "marks": 83},
    {"name": "3", "marks": 53},
    {"name": "ZRd", "marks": 93},
    {"name": "pSs", "marks": 8},
    {"name": "7dDx8sd", "marks": 98},
    {"name": "rmKFZ8X", "marks": 74},
    {"name": "esCPdDL", "marks": 0},
    {"name": "9CYCl", "marks": 48},
    {"name": "IGOu", "marks": 12},
    {"name": "H98T9AI", "marks": 51},
    {"name": "JLOwIj5xSg", "marks": 72},
    {"name": "kOS0oHv7z", "marks": 40},
    {"name": "T0", "marks": 91},
    {"name": "19WVH", "marks": 29},
    {"name": "ibVLOY", "marks": 96},
    {"name": "Ul", "marks": 59},
    {"name": "WWmQ", "marks": 24},
    {"name": "aQ2dK01cm", "marks": 10},
    {"name": "DPFFMVcVOU", "marks": 39},
    {"name": "9163qVYVi", "marks": 54},
    {"name": "T", "marks": 84}
]

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    result = {student["name"]: student["marks"] for student in data if student["name"] in name}
    return result
