class WavesMenager:
    def __init__(self):
        self.wave_index = 0
        self.create_waves()

    def create_waves(self):
        wave1 = [0, 0, 0]
        wave2 = [0, 1, 1, 0]
        wave3 = [0, 1, 0, 1, 2]

        self.waves = [wave1, wave2, wave3]

    def get_new_wave(self):
        self.wave_index += 1
        return self.waves[self.wave_index-1]

    def is_there_more_waves(self):
        return self.wave_index < len(self.waves)


