from datetime import datetime as dt

from skyfield.api import load, utc

import app.services.skyfield_client as sky
from app.exceptions import InvalidDateTime, PlanetIdNotFound


def calculate_planet_coords(planet_name: str, datetime_obj: dict):
    if planet_name == "MARS":
        planet = sky.eph["MARS_BARYCENTER"]
    elif planet_name == "JUPITER":
        planet = sky.jup_sys["JUPITER"]
    elif planet_name == "SATURN":
        planet = sky.sat_sys["SATURN"]
    elif planet_name == "URANUS":
        planet = sky.ura_sys["URANUS"]
    elif planet_name == "NEPTUNE":
        planet = sky.nep_sys["NEPTUNE"]
    else:
        planet = sky.eph[planet_name]

    ts = load.timescale()
    t = ts.from_datetime(
        dt(
            datetime_obj["year"],
            datetime_obj["month"],
            datetime_obj["day"],
            datetime_obj["hour"],
            datetime_obj["minute"],
            datetime_obj["second"],
            tzinfo=utc,
        )
    )

    astrometric = sky.sun.at(t).observe(planet)
    x_au, y_au, z_au = astrometric.position.au
    x_km, y_km, z_km = astrometric.position.km

    return {
        "x": {
            "au": x_au,
            "km": x_km,
        },
        "y": {
            "au": y_au,
            "km": y_km,
        },
        "z": {
            "au": z_au,
            "km": z_km,
        },
    }


def planets_id_controller(planet_id: int, datetime: str):
    if planet_id not in range(1, 9):
        raise PlanetIdNotFound(planet_id)

    try:
        parsed_dt = dt.strptime(datetime, "%m/%d/%Y %H:%M:%S").replace(tzinfo=utc)
        datetime_obj = {
            "month": parsed_dt.month,
            "day": parsed_dt.day,
            "year": parsed_dt.year,
            "hour": parsed_dt.hour,
            "minute": parsed_dt.minute,
            "second": parsed_dt.second,
        }
    except ValueError:
        raise InvalidDateTime(datetime)

    match planet_id:
        case 1:
            return {
                "planet": "Mercury",
                "coords": calculate_planet_coords("MERCURY", datetime_obj),
            }
        case 2:
            return {
                "planet": "Venus",
                "coords": calculate_planet_coords("VENUS", datetime_obj),
            }
        case 3:
            return {
                "planet": "Earth",
                "coords": calculate_planet_coords("EARTH", datetime_obj),
            }
        case 4:
            return {
                "planet": "Mars",
                "coords": calculate_planet_coords("MARS", datetime_obj),
            }
        case 5:
            return {
                "planet": "Jupiter",
                "coords": calculate_planet_coords("JUPITER", datetime_obj),
            }
        case 6:
            return {
                "planet": "Saturn",
                "coords": calculate_planet_coords("SATURN", datetime_obj),
            }
        case 7:
            return {
                "planet": "Uranus",
                "coords": calculate_planet_coords("URANUS", datetime_obj),
            }
        case 8:
            return {
                "planet": "Neptune",
                "coords": calculate_planet_coords("NEPTUNE", datetime_obj),
            }
