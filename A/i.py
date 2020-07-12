# Tower of Hanoi Problem for 'n' number of disks

def tower_of_honai(no_of_disc, start_peg, temp_peg, end_peg):
    if no_of_disc == 1:
        print(f'Move disk {no_of_disc} from {start_peg} to {end_peg}')
    else:
        tower_of_honai(no_of_disc - 1, start_peg, end_peg, temp_peg)
        print(f'Move disk {no_of_disc} from {start_peg} to {end_peg}')
        tower_of_honai(no_of_disc - 1, temp_peg, start_peg, end_peg)


print('********** TOWER OF HONAI *************')
disc = int(input('Enter no. of pegs : '))
tower_of_honai(disc, 'A', 'B', 'C')