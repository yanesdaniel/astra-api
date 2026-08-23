from skyfield.api import Loader

load = Loader("./data/ephemerides")

eph = load("de440.bsp")
jup_sys = load(
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/jup348.bsp"
)
sat_sys = load(
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/sat441.bsp"
)
ura_sys = load(
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/ura184_part-3.bsp"
)
nep_sys = load(
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/satellites/nep105.bsp"
)

sun = eph["SUN"]
