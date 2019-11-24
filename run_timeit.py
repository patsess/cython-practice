
import timeit
import pyximport; pyximport.install()


if __name__ == '__main__':
    # expr = '[{}_get_income_tax_rate(20000) for _ in range(10000)]'
    # setup_expr = ('from {}thon_functions import get_income_tax_rate as '
    #               '{}_get_income_tax_rate')
    expr = '{}_repeat_income_tax_rates(20000, 10000)'
    setup_expr = ('from {}thon_functions import repeat_income_tax_rates as '
                  '{}_repeat_income_tax_rates')

    time_dict = {}  # initialise
    for label_, lang_type_ in [('native python', 'py'), ('cython', 'cy')]:
        time_dict[lang_type_] = timeit.timeit(
            expr.format(lang_type_),
            setup=setup_expr.format(lang_type_, lang_type_),
            number=10000)
        print('{} time: {}'.format(label_, time_dict[lang_type_]))

    print('cython ran {}x faster'
          .format(time_dict['py'] / float(time_dict['cy'])))
