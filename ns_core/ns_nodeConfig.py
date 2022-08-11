class ns_nodeConfig:
    ##
    def __init__(self, e_max=100.0, e_c = 0.02, e_r = 44.0, e_th = 40 ):
        # battery capacity in joule, remaining energy 
        self.BatteryCapacity = e_max
        ## enery consumption rate 
        self.ConsumptionRate = e_c
        ## max batter_capacity 
        self.max_battery_capacity = e_max
        ## remaining energy 
        self.remain_en = e_r
        ## energy threshold
        self.en_threshold = e_th
        self.rx_packets_count = 0
        self.tx_packet_count = 0
        self.charge_requests_count =0
        self.chargeRate = 1
        self.ComRange = 50
    def update_remaining_en(self):
        if self.BatteryCapacity <=0:
            pass
        self.BatteryCapacity = self.BatteryCapacity-e_c
        return self
    def update_rx_packets(self):
        self.rx_packets_count = self.rx_packets_count+1
        return self
    def update_tx_packets(self):
        self.tx_packet_count = self.tx_packet_count+1
        return self
    def charge(self):
        if(self.BatteryCapacity >=self.max_battery_capacity):
            pass
        self.BatteryCapacity = self.BatteryCapacity+self.chargeRate
        return self
    