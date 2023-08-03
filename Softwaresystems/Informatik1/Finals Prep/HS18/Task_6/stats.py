# content of file "stats.py"
def get_system_stats():
    """Provides access to useful system stats (key -> description):
    - cpu_temp -> The temperature of the CPU sensor in "Kelvin" (float)
    - fan_speed -> The speed of the CPU fan in "rotations per minute" (int)
    - ... (several other stats, cut for brevity)
    Returns: A dictionary that contains all stats by key."""

    return {
        "cpu_temp": 349.6,
        "fan_speed": 4321,
        #...
    }

class TempReader():
    def getStats(self):
        return get_system_stats()["cpu_temp"]

    def celsius(self):
        temp = round(self.getStats() - 273.15,1)
        return f"{temp}C"

    def fahrenheit(self):
        temp = round(1.8 * self.getStats() - 459.67, 1)
        return f"{temp}F"

tr = TempReader()
print(tr.celsius())
print(tr.fahrenheit())