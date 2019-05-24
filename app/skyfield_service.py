from skyfield.api import load, Topos

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
