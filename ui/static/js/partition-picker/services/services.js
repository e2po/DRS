'use strict';
(function () {
    'use strict';

    var serviceId = 'partitionService';
    /**
     * Purpose: $description$
     */
    angular.module('eepdev.partition-picker.services').factory(serviceId, [serviceFunc]);

    function serviceFunc()
    {
        var socket = socketFactory({
            ioSocket: io.connect()
        });
        socket.forward('error');
        return socket;
    }
})();


//angular.module('PartitionPickerApp')
//    .factory('socket', function (socketFactory) {
//        var socket = socketFactory({
//            ioSocket: io.connect()
//        });
//        socket.forward('error');
//        return socket;
//    });