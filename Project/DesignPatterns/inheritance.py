import abc


class UIControl(abc.ABC):
    def enable(self):
        print('Enabled')

    def focus(self):
        print('Focus')

    @abc.abstractmethod
    def draw(self):
        return NotImplemented


class TextBox(UIControl):
    def draw(self):
        print('Drawing a textbox')


class CheckBox(UIControl):
    def draw(self):
        print('Drawing a checkbox')


def drawUIControl(control: UIControl):
    return control.draw()


if __name__ == '__main__':
    drawUIControl(TextBox())
    drawUIControl(CheckBox())
