[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# HeadR

**TL;DR**: json to html for headers

requires python >= 3.5

## Requirements

* `jinja2`

## Install

`pip install -r requirements`

## Example

```bash
python3 run.py res/rtp.json -b 1
```

> `-b 1` => 1 byte per line

result (`out.html` on 1 column):

<html>
    <body>
        <table>
            <tr>
                <th>Offsets</th>
                <th>Octet</th>
                <th colspan = "8">
                    0
                </th>
            </tr>
            <tr>
                <th>Octet</th>
                <th>Bit</th>
                <td colspan = "1">
                    0
                </td>
                <td colspan = "1">
                    1
                </td>
                <td colspan = "1">
                    2
                </td>
                <td colspan = "1">
                    3
                </td>
                <td colspan = "1">
                    4
                </td>
                <td colspan = "1">
                    5
                </td>
                <td colspan = "1">
                    6
                </td>
                <td colspan = "1">
                    7
                </td>
            </tr>
            <tr>
                <td>
                    0
                </td>
                <td>
                    0
                </td>
                    <td colspan="2">
                        version
                    </td>
                    <td colspan="1">
                        P
                    </td>
                    <td colspan="1">
                        X
                    </td>
                    <td colspan="4">
                        CC
                    </td>
            </tr>
            <tr>
                <td>
                    1
                </td>
                <td>
                    8
                </td>
                    <td colspan="1">
                        M
                    </td>
                    <td colspan="7">
                        PT
                    </td>
            </tr>
            <tr>
                <td>
                    2
                </td>
                <td>
                    16
                </td>
                    <td colspan="8">
                        Sequence number
                    </td>
            </tr>
            <tr>
                <td>
                    3
                </td>
                <td>
                    24
                </td>
                    <td colspan="8">
                        Sequence number
                    </td>
            </tr>
            <tr>
                <td>
                    4
                </td>
                <td>
                    32
                </td>
                    <td colspan="24">
                        Timestamp
                    </td>
            </tr>
            <tr>
                <td>
                    5
                </td>
                <td>
                    40
                </td>
                    <td colspan="16">
                        Timestamp
                    </td>
            </tr>
            <tr>
                <td>
                    6
                </td>
                <td>
                    48
                </td>
                    <td colspan="8">
                        Timestamp
                    </td>
            </tr>
            <tr>
                <td>
                    7
                </td>
                <td>
                    56
                </td>
                    <td colspan="8">
                        Timestamp
                    </td>
            </tr>
            <tr>
                <td>
                    8
                </td>
                <td>
                    64
                </td>
                    <td colspan="24">
                        SSRC identifier
                    </td>
            </tr>
            <tr>
                <td>
                    9
                </td>
                <td>
                    72
                </td>
                    <td colspan="16">
                        SSRC identifier
                    </td>
            </tr>
            <tr>
                <td>
                    10
                </td>
                <td>
                    80
                </td>
                    <td colspan="8">
                        SSRC identifier
                    </td>
            </tr>
            <tr>
                <td>
                    11
                </td>
                <td>
                    88
                </td>
                    <td colspan="8">
                        SSRC identifier
                    </td>
            </tr>
        </table>
    </body>
</html>

## Customize Output

see `static/styles.css`, `templates/template.html`