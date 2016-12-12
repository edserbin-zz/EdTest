# EdTest

<p> Для работы установите виртуальное окружение для python 2.7: </p>
<p> 	virtualenv -p python2.7 .env </p>
<p> Активируйте его:</p>
	source .env/bin/activate
<p> Установите требования:</p>
<p> pip install -r requirements.txt</p>


<p> !!!В связи с тем, что тесты писались с использованием selenium 3.0.2,в котором
теперь используеются драйвера выпускаемые каждым браузером отдельно под разные под свои версии
в папку drivers загружены драйвера chromedriver, geckodriver для 64-x Ubuntu.
В случае необходимости их заменить обращайтесь:
<p> почта edserbin@gmail.com </p>
<p> скайп ideyfixed </p>

<p> Из-за того что в geckodriver на текущий момент нет поддержки класса Action
возникают ошибки при использовании функции move_to_element. Данная функция была использована в
двух тестовых end to end сценариях, в итоге возникнет ее фиксация(скриншот и вывод url) </p>

<p> Для конфигурации запускаемого бразуера используется параметр в файле:
start_settings.py browser, который должен принимать значение с именем браузера </p>

<p> Для обработки упавших тестов(скриншот и вывод url) была написана функция декоратор check_failed, которая находится
в файле base_test</p>

<p> так же для проверки отправки письма было использовано api сервиса temp mail, с помощью
которого создается временная почта, на которую приходит письмо </p>

<p> В качестве тестов были выбраны два end-to-end сценария, один параметризованный тест и один "упавший" тест
для демонстрации работы описаного кода </p>
<p> Для запуска тестов используйте pytest -s (для того чтобы выводилсь url упавших тестов) </p>

<p> первый сценарий (форме сценария немного искажена из-за текстого редактора,
в случае необходимости могу переделать</p>
<ul>
<li>Перейти на сайт</li>
<li>Ввести в поиск “book”</li>
<li>Посмотреть список товаров в виде списка</li>
<li>Добавить 4 первых товара в избраное</li>
<li>Убедиться что в корзине 4 товара</li>
<li>Перейти к 4 товару</li>
<li>Удалить его из избранного</li>
<li>Убедиться что в корзине 3 товара</li>
<li>Перейти в избранное</li>
<li>Отправить письмо на почту</li>
<li>Убедиться что письмо пришло</li>
</ul>
<p> второй сценарий </p>
<ul>
<li>Перейти на сайт
<li>Ввести в поиска “book”
<li>Посмотреть список товаров в виде списка</li>
<li>Передумать, Посмотреть список товаров в виде галереи</li>
<li>Добавить 3 первых товара в избранное </li>
<li>Убедиться что в корзине 3 товара</li>
<li>Перейти к первому товару</li>
<li>Убрать его из избранного</li>
<li>Убедиться, что в корзине 2 товара</li>
<li>Перейти в избранное</li>
<li>Удалить из избранного товар 1</li>
<li>Убедиться, что в корзине 1 товар</li>

</ul>
<p> параметризированный тест </p>
<ul>
<li>Перейти на сайт </li>
<li>в бить в поиск name</li>
<li>Перейти к первому товару</li>
<li>Добавить его в избранное</li>
<li>Убедиться что в избранном один товар</li>

</ul>

<p> и упавший тест, в котором есть невыполнимое условие,
нужен для демонстрации декоратора </p>