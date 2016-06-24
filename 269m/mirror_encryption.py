

class MirrorEncrypt(object):
    def __init__(self, mirror_filename):
        self.mirror_grid = []

        with open(mirror_filename, "r") as handle:
            for line in handle:
                mirror_line = []
                for c in line:
                    if c in (" ", "\\", "/"):
                        mirror_line.append(c)
                [mirror_line.append(" ") for _ in range(len(mirror_line), 13)]

                self.mirror_grid.append(mirror_line)

    def encrypt_letter(self, letter):
        pos_row, pos_col = 0, 0
        vel_row, vel_col = 0, 0

        if letter.islower():
            if ord(letter) <= ord("m"):
                pos_row = 0
                pos_col = ord(letter) - ord("a")

                vel_row = 1
                vel_col = 0
            else:
                pos_row = ord(letter) - ord("n")
                pos_col = 12

                vel_row = 0
                vel_col = -1
        else:
            if ord(letter) <= ord("M"):
                pos_row = ord(letter) - ord("A")
                pos_col = 0

                vel_row = 0
                vel_col = 1
            else:
                pos_row = 12
                pos_col = ord(letter) - ord("N")

                vel_row = -1
                vel_col = 0

        # while "in bounds" -> keep on moving
        while pos_row in range(0, 13) and pos_col in range(0, 13):
            if self.mirror_grid[pos_row][pos_col] == "/":
                # coming from the left
                if vel_col == 1:
                    # go upwards
                    vel_col = 0
                    vel_row = -1
                # coming from the right
                elif vel_col == -1:
                    # go downwards
                    vel_col = 0
                    vel_row = 1
                # coming from above
                elif vel_row == 1:
                    # go left
                    vel_col = -1
                    vel_row = 0
                # coming from below
                elif vel_row == -1:
                    # go right
                    vel_col = 1
                    vel_row = 0

            elif self.mirror_grid[pos_row][pos_col] == "\\":
                # coming from the left
                if vel_col == 1:
                    # go downwards
                    vel_col = 0
                    vel_row = 1
                # coming from the right
                elif vel_col == -1:
                    # go upwards
                    vel_col = 0
                    vel_row = -1
                # coming from above
                elif vel_row == 1:
                    # go right
                    vel_col = 1
                    vel_row = 0
                # coming from below
                elif vel_row == -1:
                    # go left
                    vel_col = -1
                    vel_row = 0

            pos_col += vel_col
            pos_row += vel_row

        # check for A thru M
        if pos_col == -1:
            return chr(ord("A") + pos_row)
        # check for n thru Z
        elif pos_col == 13:
            return chr(ord("n") + pos_row)
        # check for a thru m
        elif pos_row == -1:
            return chr(ord("a") + pos_col)
        # finally, must be N thru Z
        elif pos_row == 13:
            return chr(ord("N") + pos_col)

        raise Exception("oops, something went wrong! isnt that a helpful error message???")

    def encrypt(self, word):
        ret = ""
        for c in word:
            ret += self.encrypt_letter(c)

        return ret

if __name__ == '__main__':
    me = MirrorEncrypt("mirror.txt")
    print(me.encrypt("DailyProgrammer"))
    print(me.encrypt("TpnQSjdmZdpoohd"))
