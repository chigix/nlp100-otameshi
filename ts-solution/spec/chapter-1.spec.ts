import * as _ from 'lodash';

test('[00]文字列の逆順', () =>
    expect('stressed'.split('').reverse().join('')).toEqual('desserts'),
);

test('[01]パタトクカシーー', () =>
    expect([].filter.call('パタトクカシーー',
        function (c: string, index: number) {
            return ~[0, 2, 4, 6].indexOf(index);
        }).join('')).toEqual('パトカー'),
);

test('[02]「パトカー」＋「タクシー」', () =>
    expect(
        _.zip('パトカー'.split(''), 'タクシー'.split(''))
            .reduce((prev, curr) => prev + curr.join(''), ''),
    ).toEqual('パタトクカシーー'),
);

test('[03]円周率', () =>
    expect(_.split('Now I need a drink, alcoholic of course,'
        + ' after the heavy lectures involving quantum mechanics.',
        ' ')
        .map(str => _.trim(str, ',. ').length))
        .toEqual([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]),
);
