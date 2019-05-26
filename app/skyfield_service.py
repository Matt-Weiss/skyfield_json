from skyfield.api import load, Topos
import datetime

class SkyfieldService():
    def ephemerides(latitude, longitude, celestial_bodies):
        planets = load('de421.bsp')
        earth = planets[399]

        mercury = planets[1]
        venus = planets[2]
        mars = planets[4]
        jupiter = planets[5]
        saturn = planets[6]
        uranus = planets[7]
        neptune = planets[8]
        pluto = planets[9]
        luna = planets[301]

        planet_hash = {
                        'mercury': mercury,
                        'venus': venus,
                        'mars': mars,
                        'jupiter': jupiter,
                        'saturn': saturn,
                        'uranus': uranus,
                        'neptune': neptune,
                        'pluto': pluto,
                        'luna': luna
                        }
        location = earth + Topos(latitude, longitude)
        ts = load.timescale()
        t = ts.now()

        results = {
                'data': {'latitude': str(latitude),
                         'longitude': str(longitude),
                         'time': t.utc_strftime('%Y-%m-%d %H:%M:%S'),
                         'celestial_bodies': []
                        }
                }

        for body in celestial_bodies:
            planet = planet_hash[body]
            astrometric = location.at(t).observe(planet)
            el, az, d = astrometric.apparent().altaz()
            ra, dec, distance = astrometric.apparent().radec()

            body_output = {
                            'name': body,
                            'decimal_attributes': {
                                                    'ra': str(ra._hours),
                                                    'dec': str(dec._degrees),
                                                    'az': str(az._degrees),
                                                    'el': str(el._degrees)
                                                  },
                            'strf_attributes': {
                                                'ra': str(ra),
                                                'dec': str(dec),
                                                'az': str(az),
                                                'el': str(el)
                                                }
                            }
            results['data']['celestial_bodies'].append(body_output)
        return results

    def telescope_tracking(latitude, longitude, celestial_body):
        planets = load('de421.bsp')
        earth = planets[399]
        mercury = planets[1]
        venus = planets[2]
        mars = planets[4]
        jupiter = planets[5]
        saturn = planets[6]
        uranus = planets[7]
        neptune = planets[8]
        pluto = planets[9]
        luna = planets[301]

        planet_hash = {
                        'mercury': mercury,
                        'venus': venus,
                        'mars': mars,
                        'jupiter': jupiter,
                        'saturn': saturn,
                        'uranus': uranus,
                        'neptune': neptune,
                        'pluto': pluto,
                        'luna': luna
                        }
        location = earth + Topos(latitude, longitude)
        ts = load.timescale()

        start_time = ts.now()
        start_time_utc_strftime = start_time.utc_strftime('%Y-%m-%d %H:%M:%S')

        end_time_utc = start_time.utc_datetime() + datetime.timedelta(0,3600)
        end_time = ts.utc(end_time_utc)
        end_time_utc_strftime = end_time.utc_strftime('%Y-%m-%d %H:%M:%S')

        planet = planet_hash[celestial_body]

        start_astrometric = location.at(start_time).observe(planet)
        start_ra, start_dec, start_distance = start_astrometric.apparent().radec()

        end_astrometric = location.at(end_time).observe(planet)
        end_ra, end_dec, end_distance = end_astrometric.apparent().radec()

        results = {
                    'data': {'latitude': str(latitude),
                             'longitude': str(longitude),
                             'start_time': start_time_utc_strftime,
                             'end_time': end_time_utc_strftime,
                             'celestial_body': celestial_body,
                             'start_dec': str(start_dec._degrees),
                             'start_ra': str(start_ra._hours),
                             'end_dec': str(end_dec._degrees),
                             'end_ra': str(end_ra._hours)
                            }
                    }

        return results

# 0 SOLAR SYSTEM BARYCENTER,
# 1 MERCURY BARYCENTER,
# 2 VENUS BARYCENTER,
# 3 EARTH BARYCENTER,
# 4 MARS BARYCENTER,
# 5 JUPITER BARYCENTER,
# 6 SATURN BARYCENTER,
# 7 URANUS BARYCENTER,
# 8 NEPTUNE BARYCENTER,
# 9 PLUTO BARYCENTER,
# 10 SUN,
# 199 MERCURY,
# 399 EARTH,
# 299 VENUS,
# 301 MOON,
# 499 MARS"
