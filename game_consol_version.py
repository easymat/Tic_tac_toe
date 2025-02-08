from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result):
    with open('results.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def main():
    # Создать игровое поле - объект класса Board.
    game = Board()
    current_player = 'X'
    running = True
    # Отрисовать поле в терминале.
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                col = int(input('Введите номер столбца: '))
                if col < 0 or col >= game.field_size:
                    raise FieldIndexError
                if game.board[row][col] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}'
                )
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        # Разместить на поле символ по указанным координатам - сделать ход.
        game.make_move(row, col, current_player)
        print('Ход сделан!')
        # Перерисовать поле с учётом сделанного хода.
        game.display()

        if game.check_win(current_player):
            result = f'Победили {current_player}'
            print(result)
            save_result(result)
            running = False

        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
