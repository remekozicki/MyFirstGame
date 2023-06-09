class WavesMenager:
    def __init__(self):
        self.wave_index = 0
        self.create_waves()

    def create_waves(self):
        wave0 = [0, 0]
        wave1 = [0, 0, 0]
        wave2 = [0, 1, 0, 0, 0]
        wave3 = [0, 1, 0, 1, 1]
        wave4 = [0, 2, 1, 0, 1, 0, 1, 1]
        wave5 = [2, 1, 0, 2, 2, 1, 0, 1, 2, 0, 1]
        wave6 = [2, 1, 0, 2, 2, 1, 0, 1, 2, 2, 1, 2, 2, 2]
        wave7 = [2, 2, 2, 2, 0, 2, 0, 2, 2, 1, 1, 2, 2, 2, 0, 0, 1]
        wave8 = [2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 2, 2, 2, 0, 0, 1, 2, 2, 0, 2, 2, 2, 2, 2]
        wave9 = [0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 1, 2, 0, 0, 1, 2, 2, 0, 2, 2, 2, 2]

        self.waves = [wave0, wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9]

    def get_new_wave(self):
        self.wave_index += 1
        return self.waves[self.wave_index-1]

    def is_there_more_waves(self):
        return self.wave_index < len(self.waves)
