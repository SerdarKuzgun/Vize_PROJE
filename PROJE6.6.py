import random
from abc import ABC, abstractmethod

# Soyut Sınıflar
class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.score = 0

    @abstractmethod
    def make_move(self):
        pass

class ComputerPlayer(ABC):
    def __init__(self):
        pass

# Somut Sınıflar
class HumanPlayer(Player):
    def make_move(self):
        move = input("Taş, Kağıt, veya Makas seçin: ").lower()
        while move not in ['taş', 'kağıt', 'makas']:
            move = input("Geçersiz seçim! Taş, Kağıt, veya Makas seçin: ").lower()
        return move

class RandomComputerPlayer(ComputerPlayer):
    def make_move(self):
        return random.choice(['taş', 'kağıt', 'makas'])

# Oyun Mantığı
class Game:
    def __init__(self):
        self.human_player = None
        self.computer_player = RandomComputerPlayer()
        self.history = []

    def get_winner(self, human_move, computer_move):
        if human_move == computer_move:
            return None  # Beraberlik
        elif (human_move == 'taş' and computer_move == 'makas') or \
             (human_move == 'kağıt' and computer_move == 'taş') or \
             (human_move == 'makas' and computer_move == 'kağıt'):
            return self.human_player
        else:
            return self.computer_player

    def play(self):
        human_name = input("Oyuncunun adını girin: ")
        self.human_player = HumanPlayer(human_name)

        while True:
            human_move = self.human_player.make_move()
            computer_move = self.computer_player.make_move()

            print(f"{self.human_player.name} seçimi: {human_move}")
            print(f"Bilgisayar seçimi: {computer_move}")

            winner = self.get_winner(human_move, computer_move)

            if winner is None:
                print("Sonuç: Beraberlik!")
            elif winner == self.human_player:
                print(f"Sonuç: {self.human_player.name} kazandı!")
                self.human_player.score += 1
            else:
                print("Sonuç: Bilgisayar kazandı!")
                self.computer_player.score += 1

            self.history.append((self.human_player.name, human_move, "Bilgisayar", computer_move))

            print(f"{self.human_player.name} Puanı: {self.human_player.score}, Bilgisayar Puanı: {self.computer_player.score}")

            continue_game = input("Devam etmek istiyor musunuz? (E/H): ").lower()
            if continue_game != 'e':
                break

        print("\nOyun Geçmişi:")
        for entry in self.history:
            print(f"{entry[0]}: {entry[1]} - {entry[2]}: {entry[3]}")

# Oyun başlatma
if __name__ == "__main__":
    game = Game()
    game.play()
