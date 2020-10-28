from PyViCare.PyViCareDevice import Device

class Solar(Device):

    def getSolarActive(self):
        try:
            return self.service.getProperty("heating.solar")["properties"]["active"]["value"]
        except KeyError:
            return "error"

    def getSolarCircuitStatus(self):
        try:
            return self.service.getProperty('heating.solar.pumps.circuit')["properties"]["status"]["value"]
        except KeyError:
            return "error"

    def getSolarRechargeSuppressionStatus(self):
        try:
            return self.service.getProperty("heating.solar.rechargeSuppression")["properties"]["status"]["value"]
        except KeyError:
            return "error"

    def getSolarChargingActive(self):
        try:
            return self.service.getProperty("heating.dhw.charging")["properties"]["active"]["value"]
        except KeyError:
            return "error"

    def getSolarCollectorTemperature(self):
        try:
            return self.service.getProperty("heating.solar.sensors.temperature.collector")["properties"]["value"][
                "value"]
        except KeyError:
            return "error"

    def getSolarWaterTemperature(self):
        try:
            return self.service.getProperty("heating.solar.sensors.temperature.dhw")["properties"]["value"][
                "value"]
        except KeyError:
            return "error"

    def getSolarProductionToday(self):
        try:
            return self.service.getProperty('heating.solar.power.production')['properties']['day']['value'][0]
        except KeyError:
            return "error"

    def getSolarProductionDays(self):
        try:
            return self.service.getProperty('heating.solar.power.production')['properties']['day']['value']
        except KeyError:
            return "error"

    def getSolarProductionWeeks(self):
        try:
            return self.service.getProperty('heating.solar.power.production')['properties']['week']['value']
        except KeyError:
            return "error"

    def getSolarProductionMonths(self):
        try:
            return self.service.getProperty('heating.solar.power.production')['properties']['month']['value']
        except KeyError:
            return "error"

    def getSolarProductionYears(self):
        try:
            return self.service.getProperty('heating.solar.power.production')['properties']['year']['value']
        except KeyError:
            return "error"

    def getSolarcumulativeProduced(self):
        try:
            return self.service.getProperty('heating.solar.power.cumulativeProduced')['properties']['value']
        except KeyError:
            return "error"

    def getSolarHours(self):
        try:
            return self.service.getProperty('heating.solar.statistics')['properties']['hours']['value']
        except KeyError:
            return "error"
