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

        location = earth + Topos(latitude, longitude)

        # for body in celestial_bodies:
        #     astrometric = location.at(t).observe(mars)
        #     alt, az, d = astrometric.apparent().altaz()

        ts = load.timescale()
        t = ts.now()
        return 1

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
