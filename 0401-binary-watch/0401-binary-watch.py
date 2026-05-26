class Solution:
    def readBinaryWatch(self, turnedOn: int):

        result = []

        # Hours: 0 -> 11
        for hour in range(12):

            # Minutes: 0 -> 59
            for minute in range(60):

                # Count total number of 1 bits
                total_bits = (
                    bin(hour).count('1') +
                    bin(minute).count('1')
                )

                # If LEDs ON match
                if total_bits == turnedOn:

                    # Format minute with leading zero
                    time = f"{hour}:{minute:02d}"

                    result.append(time)

        return result