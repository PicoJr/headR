# HeadR

**TL;DR**: json to html for headers

## Example

```bash
python3 run.py res/rtp.json
```

result (`out.html`):

<html>
<body>
<table>
    <tr>
        <th>Offsets</th>
        <th>Octet</th>
        <th colspan="8">
            0
        </th>
        <th colspan="8">
            1
        </th>
        <th colspan="8">
            2
        </th>
        <th colspan="8">
            3
        </th>
    </tr>
    <tr>
        <th>Octet</th>
        <th>Bit</th>
        <td colspan="1">
            0
        </td>
        <td colspan="1">
            1
        </td>
        <td colspan="1">
            2
        </td>
        <td colspan="1">
            3
        </td>
        <td colspan="1">
            4
        </td>
        <td colspan="1">
            5
        </td>
        <td colspan="1">
            6
        </td>
        <td colspan="1">
            7
        </td>
        <td colspan="1">
            8
        </td>
        <td colspan="1">
            9
        </td>
        <td colspan="1">
            10
        </td>
        <td colspan="1">
            11
        </td>
        <td colspan="1">
            12
        </td>
        <td colspan="1">
            13
        </td>
        <td colspan="1">
            14
        </td>
        <td colspan="1">
            15
        </td>
        <td colspan="1">
            16
        </td>
        <td colspan="1">
            17
        </td>
        <td colspan="1">
            18
        </td>
        <td colspan="1">
            19
        </td>
        <td colspan="1">
            20
        </td>
        <td colspan="1">
            21
        </td>
        <td colspan="1">
            22
        </td>
        <td colspan="1">
            23
        </td>
        <td colspan="1">
            24
        </td>
        <td colspan="1">
            25
        </td>
        <td colspan="1">
            26
        </td>
        <td colspan="1">
            27
        </td>
        <td colspan="1">
            28
        </td>
        <td colspan="1">
            29
        </td>
        <td colspan="1">
            30
        </td>
        <td colspan="1">
            31
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
        <td colspan="1">
            M
        </td>
        <td colspan="7">
            PT
        </td>
        <td colspan="16">
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
        <td colspan="32">
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
        <td colspan="32">
            SSRC identifier
        </td>
    </tr>
</table>
</body>
</html>

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
